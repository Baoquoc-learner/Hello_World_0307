# Writing to a File
# Writing a Single Line

from pathlib import Path
# path = Path('programming.txt')
# path.write_text('I love programming, i love tiktok.')
print("\t--------------------------------------------------------------------")
# Writing multiple Lines
contents = "I love programming.\n"
contents += "I love youtube.\n"
contents += "I love Facebook.\n"
contents += "I love Vietnam.\n"
Content = Path('programming.txt')
Content.write_text(contents)
