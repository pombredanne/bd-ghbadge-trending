from bitdeli.chain import Profiles
import random

def repos(profiles):
    repos = {}
    for profile in profiles:
        for repo in profile['repos']:
            repos[repo] = random.randint(0, 3)
    yield [{'repo': repo, 'badge': 'gh-trend-%d' % t}
           for repo, t in repos.iteritems()]
    
Profiles().map(repos).show('table',
                           size=(12, 6),
                           json_export=True)
        
    
