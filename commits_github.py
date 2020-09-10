import requests


def get_commits_messages(user, repo, last_n=100):
    if last_n > 100:
        raise Exception(f'Can\'t get more than 100 commits with get_commits_messages function,'
                        f' but asked for {last_n}')

    base_url = 'https://api.github.com'
    response = requests.get(f'{base_url}/repos/{user}/{repo}/commits?per_page={last_n}')
    response.raise_for_status()

    # Assume response use JSON, as it said in v3 github api documentation
    # TODO: add try / catch on response.json()

    return [commit_data['commit']['message'] for commit_data in response.json()]


"""
If you want to download commits messages not from master branch
You should access branch & get last commit sha firstly
Implementation:
"""
def get_branch_commits_messages(user, repo, branch):
    base_url = 'https://api.github.com'
    branch_response = requests.get(f'{base_url}/repos/{user}/{repo}/branches/{branch}')
    branch_response.raise_for_status()

    commit_sha = branch_response.json()['commit']['sha']
    commits_response = requests.get(f'{base_url}/repos/'
                                    f'{user}/{repo}/'
                                    f'commits?per_page=100&sha={commit_sha}')
    commits_response.raise_for_status()

    return [item['commit']['message'] for item in commits_response.json()]
