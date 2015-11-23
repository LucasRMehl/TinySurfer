# TinySurfer

A tiny web browser. Whatever version of WebKit it is that comes with PyQt4 does
most of the work, but this adds a surprising amount of functionality in only 53
lines of code.

The first version was based on this:

http://thecodeinn.blogspot.com/2013/08/tutorial-pyqt-web-browser.html

But later I found this, which uses more of QWebKit's built-in functionality:

http://ralsina.me/weblog/posts/BB948.html

The current version of this is mostly what you'll find on that second link.  I
just de-obfuscated the one bit of lambda abuse, because I think otherwise it's
a solid piece of code for learning purposes.  The original author (Roberto
Alsina), wrote in a comment on that page that the code is under an MIT license.
I'm using the same license.

Here is the original author's later versions of the code on GitHub:

https://github.com/ralsina/devicenzo

So, you might ask, why did I do this?

I actually needed something like this for work: I was working remotely on a
heavy-duty CentOS Linux box that had no graphical browsers installed, but a new
piece of hardware recently installed used a web interface.  In the lab we can
bring it up on a Windows box, but it had remote access disabled.  I probably
could have built Firefox or tried to find a portable Linux version or
something, but our tools already used PyQt4, so why not?

I can't promise anyone else will ever run into this obscure use case, but it
certainly helped me.

## ~~To-Do~~ Exercises Left to the Reader

1. Add some bookmarking functionality.  I wanted to get this in before the
   initial commit, but it's the end of the weekend.  I wanted to add something
   a little more interesting (e.g. categories) than the one implemented in the
   first link.
   
2. Add tabs.  If you look at the original author's GitHub page, he's got this
   functionality, but I'd rather make each tab run in a separate process.
   
3. Upgrade to PyQt5.  PyQt4's WebKit apparently leaks memory, so use the
   current incarnation at your own risk!
