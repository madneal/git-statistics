from git import Repo
from os import listdir
from os.path import exists


git_parent_dir = "C:/Users/neal1/project"

git_dir_list = []

for path in listdir(git_parent_dir):
    git_dir_list.append(path)


for git_dir in git_dir_list:
    git_config_file = git_parent_dir + "/" + git_dir + "/.git/"
    if exists(git_config_file):
        print(git_config_file)
        repo = Repo.init(git_dir)
        print(repo.is_dirty())
        git = repo.git
        git.branch("master")
        git.log()