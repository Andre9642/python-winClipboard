# coding: UTF-8
from __future__ import unicode_literals
import sys
import winClipboard
isPy3 = True if sys.version_info >= (3, 0) else False

print("Python %s" % sys.version)
tests = [
	((
		"<h1>Test</h1>"
		"<p>This is a simple test in HTML. αβ∉√∩∪∫😀</p>"
		"<ul><li>Python "+sys.version+"</li><li>test 1234</li></ul>"
	), True),
	(u'\ud800', True),
	("Hello World! 😆 αβ∉√∩∪∫", False),
	(u'\ud800', False)
]

iTest = 1
for test in tests:
	copy = winClipboard.copyHTML if test[1] else winClipboard.copyText
	get = winClipboard.getHTML if test[1] else winClipboard.getText
	copy(test[0])
	res = (get() == test[0])
	print("Test %d (%s): %s" % (iTest, ("HTML" if test[1] else "text"), ("OK" if res else "KO")))
	if not res:
		print("received: %s" % get())
		print("Excepcted: %s" % test[0])
	iTest += 1
	pause = input if isPy3 else raw_input
	pause("Press enter to continue")
