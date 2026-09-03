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

### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init`
- `git status`
- `git add`
- `git commit`
- `git log`
- `git diff`

### 1.7 Repository link

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
- How does the set-based approach check for a duplicate?
- What is the runtime and memory trade-off of each?

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge