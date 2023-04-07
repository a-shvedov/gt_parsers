from github import Github
import time
import sys

#получение избранных репо конкретного пользователя
g = Github("github_api_token")

with open("input.txt", "r") as f:
    #read the list of repository links from the file
    repo_links = f.readlines()

#open the output file for writing
with open("output.txt", "w") as f_out:
    #loop through each repository link
    for repo_link in repo_links:
        # extract the username and repository name from the link
        username, repo_name = repo_link.strip().split("/")[-2:]

        #get the user object for the repository owner
        user = g.get_user(username)
        
        #print the user's name and bio
        print(f"Username: {user.name}")
        print(f"Bio: {user.bio}")

        #get the repository object for the repository
        repo = user.get_repo(repo_name)

        #get all the stargazers for the repository
        stargazers = repo.get_stargazers()

        print(f"Count of stargazers for {repo_name}: {repo.stargazers_count}")
        
        #print the usernames of each stargazer
        print("Stargazers:")
        for stargazer in stargazers:
            print("https://github.com/" + stargazer.login)
        
        print(f"\nPassed: https://github.com/{username}\n")
        time.sleep(1)

        #write the username of each stargazer to the output file
        for stargazer in stargazers:
            f_out.write("https://github.com/" + stargazer.login + "\n")
