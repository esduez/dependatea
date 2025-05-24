from collections import defaultdict

def calculate_rewards(dependencies: dict) -> dict:
    contributors = defaultdict(int)
    for pkg, deps in dependencies.items():
        contributors[pkg] += 1
        for dep in deps:
            contributors[dep] += 1
    total = sum(contributors.values())
    return {contributor: (count/total)*1000 for contributor, count in contributors.items()}