import requests


def get_commits_messages(user, repo, last_n=100):
    if last_n > 100:
        raise Exception(f'Can\'t get more than 100 commits with get_commits_messages function,'
                        f' but asked for {last_n}')

    base_url = 'https://api.github.com'
    response = requests.get(f'{base_url}/repos/{user}/{repo}/commits?per_page={last_n}')

    # This is not "production"-like behaviour, this exception must be caught,
    # But in case of mini-test-task, I think raising an error is an appropriate way to handle this.
    response.raise_for_status()

    # Assume response use JSON, as it said in v3 github api documentation
    # In case the JSON decoding fails, response.json() raises an exception.
    # What you should do in real project: add try / catch on response.json()
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
