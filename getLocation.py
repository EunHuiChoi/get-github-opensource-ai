from github import Github

ACCESS_TOKEN = '9e7d561f7546d14a0c8e9013c543043ad73e2ca8'
g = Github(ACCESS_TOKEN)

# print(g.get_user().get_repos())

repo_name = 'tensorflow/tensorflow'
repo_list = ['apache/incubator-mxnet', 'BVLC/caffe', 'facebookarchive/caffe2', 'keras-team/keras', 'microsoft/CNTK', 'pytorch/pytorch', 'scikit-learn/scikit-learn', 'tensorflow/tensorflow', 'Theano/Theano', 'torch/torch7']

for repos in repo_list:
    repo = g.get_repo(repos)
    contributors = repo.get_contributors()
    # print(repo)
    print(f'name: {repo.full_name}, url: {repo.clone_url}, stars: {repo.stargazers_count}, forks: {repo.forks_count}')
    for contributor in contributors:
        ctb_location = contributor.location
        ctb_contributions = contributor.contributions
        print(f'location: {ctb_location}, contributions: {ctb_contributions}')

# repo = g.get_repo(repo_name)
# contributors = repo.get_contributors()

# print(f'name: {repo.full_name}, url: {repo.clone_url}, stars: {repo.stargazers_count}, forks: {repo.forks_count}')

# for contributor in contributors:
#     ctb_location = contributor.location
#     ctb_contributions = contributor.contributions
#
#     print(f'location: {ctb_location}, contributions: {ctb_contributions}')


