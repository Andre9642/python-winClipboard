# coding: UTF-8
import sys
import winClipboard
isPy3 = True if sys.version_info >= (3, 0) else False

print("Python %s" % sys.version)
tests = [
	((
		"<h1>Test</h1>"
		"<p>This is a simple test in HTML. αβ∉√∩∪∫😀</p>"
		"<ul><li>Python "+sys.version+"</li><li>Item 2</li></ul>"
	), True),
	("Hello World! 😆 αβ∉√∩∪∫", False)
]

iTest = 1
for test in tests:
	winClipboard.copy(test[0], html=test[1])
	out = winClipboard.get(html=test[1])
	res = (out == test[0])
	print("Test %d (%s): %s" % (iTest, ("HTML" if test[1] else "text"), ("OK" if res else "KO")))
	if not res: print("received: %s\nExcepcted: %s" % (out, test[0]))
	iTest += 1
	pause = input if isPy3 else raw_input
	pause("Press enter to continue")
