"""
An attempt to find active subreddit names on Reddit that are still available and not registered as subverses on Voat.

List of active subreddits found here: http://metareddit.com/reddits/active/list/
Voat: http://voat.co
"""

from selenium import webdriver
import selenium
import time

def init_webdriver():

    """Starts the webdriver."""

    global driver
    driver = webdriver.Firefox()

def exit_webdriver():

    """Closes the webdriver."""

    driver.close()
    driver.quit()

def get_subreddit_list():

    """Collects all active subreddits listed on metareddit.com"""

    subreddit_list = []

    url = "http://metareddit.com/reddits/active/list/?page="

    for page in range(207):
        driver.get(url+str(page+1))
        time.sleep(1)

        for subreddit in range(50):
            try:
                subreddit_name = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[{}]/td[2]/a".format(str(subreddit+1)))
            except selenium.common.exceptions.NoSuchElementException:
                break
            subreddit_list.append(subreddit_name.text)
            print("{} collected.".format(subreddit_name.text))

    return subreddit_list

def subverse_check(lst):

    """ Check if there is an existing subverse on Voat. """

    nonexisting_subverses = []

    url = "https://voat.co/v/"

    for subreddit in lst:
        driver.get(url+subreddit)
        time.sleep(1)

        try:
            element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/span/a")
        except selenium.common.exceptions.NoSuchElementException:
            continue

        if "404" in element.text:
            nonexisting_subverses.append(subreddit)
            print("{} is not on voat.".format(subreddit))
        else:
            pass
        time.sleep(1)

    print("Found {} active subreddits that are not yet on Voat.".format(len(nonexisting_subverses)))
    return nonexisting_subverses

def save_results(textfile, lst):

    """ Save results in a file. """

    with open(textfile, "w+") as f:

        for subreddit in lst:
            f.write(subreddit+"\n")
        print("Results saved in text file.")



if __name__ == '__main__':

    init_webdriver()

    subreddit_list = get_subreddit_list()
    save_results("active_subreddits.txt", subreddit_list)

    new_subreddit_list = subverse_check(subreddit_list)
    save_results("subverses_to_create.txt", new_subreddit_list)

    exit_webdriver()



