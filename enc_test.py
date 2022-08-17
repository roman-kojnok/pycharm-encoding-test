import locale
import os
import sys
# PYTHONIOENCODING="utf-8"
# print("\U0001F609")
# sys.stdout.reconfigure(encoding='utf-8')

print(sys.stdout.encoding)
print(sys.stdout.isatty())
print(locale.getpreferredencoding())
print(sys.getfilesystemencoding())
print(os.environ["PYTHONIOENCODING"])
print(chr(246), chr(9786), chr(9787))
