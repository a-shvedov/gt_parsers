#получение избранных репо конкретного пользователя (в теле скрипта)
from github import Github

g = Github("github_pat_")

# get the user object for user
user = g.get_user("user1")
# get the repository object for repository
repo = user.get_repo("repo1")

# get all the stargazers for repository
stargazers = repo.get_stargazers()

#for stargazer in stargazers:
 #   print(stargazer.login)
 
with open("output.txt", "w") as f:
    for stargazer in stargazers:
        f.write("https://github.com/" + stargazer.login + "\n")
