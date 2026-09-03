# Lab 03: Git and GitHub
This repository documents my practice with local Git, GitHub, branches and pull requests.

## README Responses

### 1.1 After initialization
ls -la
total 8
drwxr-xr-x@ 4 UNCA  staff  128 Sep  3 10:35 .
drwxr-xr-x@ 7 UNCA  staff  224 Sep  3 10:34 ..
drwxr-xr-x@ 9 UNCA  staff  288 Sep  3 10:36 .git
-rw-r--r--@ 1 UNCA  staff  868 Sep  3 10:36 README.md

### 1.2 First git status
git status

On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

### 1.3 After the first commit
On branch main
nothing to commit, working tree clean

### 1.4 git log
aba33fa (HEAD -> main) Create lab README

### 1.5 git diff
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

--------------------------------------------------------------------------

git diff
diff --git a/README.md b/README.md
index 468274f..0442322 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,5 @@
 # Lab 03: Git and GitHub
+This repository documents my practice with local Git, GitHub, branches and pull requests.
 
 ## README Responses
 
@@ -22,8 +23,11 @@ Untracked files:
         README.md
 
 ### 1.3 After the first commit
+On branch main

How does this `git status` differ from the one in **1.2**?
in 1.2 the git status says there arent any commits yet but in 
1.5 it says there are changes that havent been staged for commit.

### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init`
this creates a new fresh git repostiory in whatever directory youre currently working in.
- `git status`
this tells you if you have unstaged changes that have been made to any of the files in your repository.
- `git add`
git add saves the changes to files you've made in your current directory and gets them ready to be staged
- `git commit`
git commit saves your staged changes locally. It's like taking a snapshot of your repo's history you can go back to at any time should a bug pop up!
- `git log`
git log shows you your commits and the associated messages that were sent up with them.
- `git diff`
git diff will show you the differences between your code since you last committed. It will show removed lines in red and added lines in green

### 1.7 Repository link
git@github.com:rizzo-unca/lab03-exercises.git

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
it walks through the array and compares each number with every other number starting with index 0 and comparing the rest of the indexes with it and so on and so forth
- How does the set-based approach check for a duplicate?
python converts the given list into a set and compares the set length to the original list and if the set is smaller it knows theres a duplicate since python sets can't have duplicates in them
- What is the runtime and memory trade-off of each?
nested loop runs on O(n^2) time whilst set based runs in O(n) time. The nested approach is significantly slower but uses a lot less memmory because it's just doing simple comparisons. The set-based approach has to create new sets for each set of data so it uses a lot more memory.

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge