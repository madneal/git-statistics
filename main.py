from git import Repo
import re
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import exists


git_parent_dir = "C:/Users/neal1/project"
GIT_LOG = r'(\d+)\D+(\d+)\D+'

git_dir_list = []

def getlog(log, name):
    log_obj = {
        "name": name,
        "added": 0,
        "removed": 0,
        "total": 0
    }
    log_arr = log.split('\n')
    for e in log_arr:
        log_re = re.compile(GIT_LOG)
        result = log_re.search(e)
        if result:
            log_obj["added"] += int(result.group(1))
            log_obj["removed"] += int(result.group(2))
            log_obj["total"] = log_obj["added"] - log_obj["removed"]
    return log_obj

for path in listdir(git_parent_dir):
    git_dir_list.append(path)


def getGitObjList(username):
    list = []
    for git_dir in git_dir_list:
        git_config_file = git_parent_dir + "/" + git_dir + "/.git/"
        if exists(git_config_file):
            print(git_config_file)
            repo = Repo(git_config_file)
            git = repo.git
            heads = repo.head
            master = heads.reference
            if master:
                log = git.log('--since=2017-01-01', '--author=' + username, '--pretty=tformat:', '--numstat')
                # print(log)
                git_obj = getlog(log, git_dir)
                list.append(git_obj)
    return list

def drawPlot(list):
    added = []
    removed = []
    total = []
    x_ticks = []
    for git_info in list:
        if (git_info["added"] > 0):
            added.append(git_info["added"])
            removed.append(git_info["removed"])
            total.append(git_info["total"])
            x_ticks.append(git_info["name"])
    groups = len(added)
    fig, ax = plt.subplots()
    index = np.arange(groups)
    bar_width = 0.3
    rect1 = plt.bar(index, added, bar_width, color='g', label='added')
    rect2 = plt.bar(index + bar_width, removed, bar_width, color='r', label='removed')
    rect3 = plt.bar(index + bar_width * 2, total, bar_width, color='b', label='total')

    plt.xlabel('Respositories')
    plt.ylabel('commits')
    # plt.xticks(index + bar_width * 3, x_ticks)
    plt.legend()
    plt.tight_layout()
    plt.show()





if __name__ == '__main__':
    git_info_list = getGitObjList('neal1991')
    for git_info in git_info_list:
        if (git_info["added"] > 0):
            print(git_info)
    drawPlot(git_info_list)

