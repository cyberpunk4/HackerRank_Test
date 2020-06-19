import os, re


def getFoldersNames(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.idea', '.vscode'):
            folders.append(item)
    return folders


def getFilesNames(path):
    files = os.listdir(path)
    return files


def getProblemURLandScore(path):
    with open(path, 'r', encoding='utf-8') as inFile:
        url = inFile.readline().split()[-1]
        difficulty = inFile.readline().split()[-1]
        score = inFile.readline().split()[-1]
        return url, difficulty, score


def getTotalNumberOfProblems():
    totalNumber = 0
    folders = getFoldersNames(os.getcwd())
    for folder in folders:
        parent_folders = getFoldersNames(os.path.join(os.getcwd(), folder))
        for parent_folder in parent_folders:
            child_folders = getFoldersNames(os.path.join(os.getcwd(), folder, parent_folder))
            for child_folder in child_folders:
                totalNumber += len(getFilesNames(os.path.join(os.getcwd(), folder, parent_folder, child_folder)))
    return totalNumber


readmeFile = open('README.md', 'w', encoding='utf-8')
print('<div align="center">'
      '<a href="https://www.hackerrank.com/gorogo106" target="_blank"><img src="HackerRank%20Logo.png" width="450" height="auto"></a>',
      file=readmeFile)
print(file=readmeFile)
print(
    '[![Author](https://img.shields.io/badge/author-gorogo106-brightgreen.svg?style=flat-square)](https://www.hackerrank.com/gorogo106)'
    '[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)'
    '</div>'
    '<br/>'
    '<br/>', file=readmeFile)
print(file=readmeFile)
print('# Solutions to Hackerrank practice problems', file=readmeFile)
print('This repository contains ' + str(
    getTotalNumberOfProblems()) + ' solutions to Hackerrank practice problems with Python 3, C++ and Oracle SQL.',
      file=readmeFile)
print(file=readmeFile)
print('Updated daily :) If it was helpful please press a star.', file=readmeFile)
print(file=readmeFile)
folders = getFoldersNames(os.getcwd())
print("# Table of Contents",file=readmeFile)
for index,folder in sorted(enumerate(folders)):
    print(str(index+1)+". "+"["+folder+"]"+"(#"+folder.lower()+")",file=readmeFile)
print(file=readmeFile)
for folder in sorted(folders):
    print('# ' + folder, file=readmeFile, end="\n")
    print("|Subdomain|Challenge|Difficulty|Score|Solution|", file=readmeFile, end="\n")
    print("|-|-|-|-|-|", file=readmeFile, end="\n")
    parent_folders = getFoldersNames(os.path.join(os.getcwd(), folder))
    for parent_folder in sorted(parent_folders):
        child_folders = getFilesNames(os.path.join(os.getcwd(), folder, parent_folder))
        for child_folder in sorted(child_folders):
            files = getFilesNames(os.path.join(os.getcwd(), folder, parent_folder, child_folder))
            for file in files:
                if file.endswith(('.cpp', '.py', '.sql', '.java')):
                    url, difficulty, score = getProblemURLandScore(
                        os.path.join(os.getcwd(), folder, parent_folder, child_folder, file))
                    # https://github.com/cyberpunk4/HackerRank_Test/blob/master/
                    print("|" + re.findall(r"[a-zA-Z -!?_]*", parent_folder)[3].strip() + "|"
                          + "[" + re.findall(r"[a-zA-Z -!?_]*",
                                             child_folder)[3].strip() + "]" + "(" + url + ")" + "|"
                          + difficulty + "|"
                          + str(score) + "|"
                          + "[Solution]"
                          + "("
                          + folder.replace(" ", "%20") + "/"
                          + parent_folder.replace(" ", "%20") + "/"
                          + child_folder.replace(" ", "%20") + "/"
                          + file.replace(" ", "%20") + ")" + "|"
                          , file=readmeFile, end="\n")
readmeFile.close()
