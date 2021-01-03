from github import Github
import main as m
import numpy as np
import pandas as pd

ACCESS_TOKEN = '5590c7618b16a2c934306e4ac0ce5ee74e4aa437'
g = Github(ACCESS_TOKEN)


class Repo:
    def __init__(self, name, des, owner_name, owner_location, topic, url, star, fork):
        self.name = str(name)
        self.des = str(des)
        self.owner_name = str(owner_name)
        self.owner_location = str(owner_location)
        self.topic = list(topic)
        self.url = str(url)
        self.star = int(star)
        self.fork = int(fork)
        self.list = [self.name, self.des, self.owner_name, self.owner_location, self.topic, self.url, self.star, self.fork]


# def create_list(value):
#     repo_list = list()
#     repo_list.append(value)
#     print(repo_list)


keywords = ['Artificial Intelligence', 'Machine Learning',
            'Deep Learning', 'Reinforcement Learning',
            'Predictive Analytics', 'Supervised Learning',
            'Unsupervised Learning', 'Neural Networks',
            'Natural Language Processing', 'Robotics',
            'Computer Vision', 'Image Recognition',
            'Facial Recognition', 'Face Recognition',
            'Self Driving', 'Speech Recognition',
            'Intelligence Systems', 'Virtual Assistant', 'Autonomous vehicle']


# for keyword in keywords:
repos = m.search_github('Artificial Intelligence')
print(repos)
for i in range(len(repos)):
    test = list()
    test.append(repos[i].name)
    print(test)

    # for repo in repos:
    #     repo_dic = {}
    #     repo_list = list()
    #
    #     repo_instance = Repo(repo.name, repo.description, repo.owner.name, repo.owner.location, repo.get_topics(), repo.url, repo.stargazers_count, repo.forks_count)
    #     repo_name_list = ['name', 'description', 'owner', 'owner_location', 'topic', 'url', 'num_stars', 'num_forks']

        # print(repo_instance.list[0])

        # series = pd.Series(repo_instance.list, index=repo_name_list)
        # df = pd.DataFrame(series)




