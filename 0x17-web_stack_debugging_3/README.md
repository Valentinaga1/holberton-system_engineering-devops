# 0x17. Web stack debugging #3

# Learning Objectives

* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

### [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp)
Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).