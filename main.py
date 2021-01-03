from github import Github
import pandas as pd

ACCESS_TOKEN = '9e7d561f7546d14a0c8e9013c543043ad73e2ca8'
# ACCESS_TOKEN = '5590c7618b16a2c934306e4ac0ce5ee74e4aa437'
g = Github(ACCESS_TOKEN)

print(f'remaining: {g.get_rate_limit().search.remaining}\nlimit: {g.get_rate_limit().search.limit}\nreset: {g.get_rate_limit().search.reset}\n')

star = '0'
year = '2019'
month_1 = '01'
month_2 = '01'

keywords = [
            'Artificial Intelligence',
            'Machine Learning',
            'Deep Learning',
            'Reinforcement Learning',
            'Predictive Analytics',
            'Supervised Learning',
            'Unsupervised Learning',
            'Neural Networks',
            'Natural Language Processing',
            'Robotics',
            'Computer Vision',
            'Image Recognition',
            'Facial Recognition',
            'Face Recognition',
            'Self Driving',
            'Speech Recognition',
            'Intelligence Systems',
            'Virtual Assistant',
            'Autonomous vehicle'
            ]


def search_github(keyword):
    repo_name_list = ['repo_name', 'description', 'owner', 'owner_location', 'topic', 'url', 'num_stars', 'num_forks']
    name_list = list()
    des_list = list()
    owner_name_list = list()
    owner_location_list = list()
    topic_list = list()
    url_list = list()
    stars_list = list()
    forks_list = list()

    query = f'+{keyword} stars:{star} created:2019-{month_1}-01..2019-{month_2}-31'
    result = g.search_repositories(query, 'stars', 'desc')

    count = result.totalCount
    print(f'Found <{keyword}> {year} created: {count} repos')

    for repo in result:
        # print(repo)
        name_list.append(repo.name)
        des_list.append(repo.description)
        owner_name_list.append(repo.owner.name)
        owner_location_list.append(repo.owner.location)
        topic_list.append(repo.get_topics())
        url_list.append(repo.clone_url)
        stars_list.append(repo.stargazers_count)
        forks_list.append(repo.forks_count)

    s1 = pd.Series(name_list)
    s2 = pd.Series(des_list)
    s3 = pd.Series(owner_name_list)
    s4 = pd.Series(owner_location_list)
    s5 = pd.Series(topic_list)
    s6 = pd.Series(url_list)
    s7 = pd.Series(stars_list)
    s8 = pd.Series(forks_list)

    df = pd.DataFrame(s1)
    df.columns = [repo_name_list[0]]
    df[repo_name_list[1]] = s2
    df[repo_name_list[2]] = s3
    df[repo_name_list[3]] = s4
    df[repo_name_list[4]] = s5
    df[repo_name_list[5]] = s6
    df[repo_name_list[6]] = s7
    df[repo_name_list[7]] = s8

    return df


for keyword in keywords:
    df = search_github(keyword)
    # print(create_csv)
    df.to_csv(f"{keyword} {star}star {month_1},{month_2}month.csv", index=False)




