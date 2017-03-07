#######################################################
# SnipShare - by Brock Campbell 2016.
# 
# This Sublime Text 3 Plugin was made to make it easier
# for developers to recall short segments of code that
# they used in the past to solve particular tasks.
# 
# The original source code can be modified and used, as 
# long as the original author is credited.
#######################################################

import sublime
import sublime_plugin
import os,sys

from os.path import expanduser


USER_FOLDER = "~/.config/sublime-text-3/Packages/User"
TRIGGER_SEPARATOR = "-"


with cd(USER_FOLDER):
	if not os.path.exists("Snippets"):
		os.makedirs("Snippets")
SNIPPET_FOLDER = USER_FOLDER + "/Snippets"

#TODO: fix quotes in snippets.
#TODO: make it able to create snippets folder.
class snipshareCommand(sublime_plugin.WindowCommand):
	tabTrigger = ""
	content = ""
	scope = ""

	def run(self):
		""" Function that is run first when the plugin is called """
		# Gets the currently selected text in the active window and prompts for user input to name the snippet.
		# Also records the scope/ what language is being programmed so snippets won't be recalled for incompatible languages.
		window = self.window
		view = window.active_view()
		self.scope = view.scope_name(view.sel()[-1].b)
		sel = view.sel()
		region1 = sel[0] 	#Multiple regions of text can be selected.
		selectionText = view.substr(region1)
		self.content = selectionText

		# Need to get "Text Trigger" - what will be typed to recall the snippet later on.
		if (self.content != ""):
			self.window.show_input_panel("Description for code snippet:", "", self.on_done, None, None)

	def on_done(self,text):
		""" When the input panel is closed or enter is pressed, this function is ran """
		# If a name for the snippet has been entered, save the snippet to file. Otherwise, prompt for input again.

		if (text == ""):
			self.window.show_input_panel("Description for code Snippet:","",self.on_done,None,None)
		else:
			self.tabTrigger = text
			if (self.tabTrigger != ""):
				self.createSnippet(self.tabTrigger,self.content)

	def createSnippet(self,tabTrigger,content):
		""" This function is used to save a code snippet to a file in a format that can be recognized by Sublime Text. """

		with cd(SNIPPET_FOLDER):
			# Set name, description and scope for the code snippet.
			print (os.getcwd())
			name = self.CamelCase(tabTrigger)
			name += ".sublime-snippet"
			description = tabTrigger
			scope = (self.scope[0:self.scope.find(' ')])
			if not os.path.exists(scope):
				os.makedirs(scope)
			path = scope + "/" + name
			
			# Replace spaces with the user-defined trigger separator.
			trigger = ""
			for c in tabTrigger:
				if (c == " "):
					trigger += TRIGGER_SEPARATOR
				else:
					trigger += c
			formatted_content = self.fixTabs(content)

			# Create a new snippet file and store it's information in it.
			f = open(path, "w")
			print("<snippet>",file=f)
			print("\t<content><![CDATA[" + formatted_content + "]]></content>",file=f)
			print("\t<tabTrigger>" + trigger + "</tabTrigger>",file=f)
			print("\t<description>" + description + "</description>",file=f)
			print("\t<scope>" + scope + "</scope>",file=f)
			print("</snippet>",file=f)
			f.close()

	def CamelCase(self, string):
		""" This function converts a string to CamelCase format """

		name = ''.join(x for x in string.title() if not x.isspace())
		return name		

	def fixTabs(self, content):
		""" This function fixes spacing issues when creating snippets with code that has tabbing. """
		
		num_tabs = 0
		lines = content.splitlines()

		# Count tabs each line is tabbed by (assuming the first line is the least-indented line).
		for c in lines[0]:
			if (c == '\t'):
				num_tabs+=1
			else:
				break

		# Remove the recorded number of tabs on each line.
		newlines = ""
		for line in lines:
			newlines += line[num_tabs:] + '\n'

		return newlines

class cd:
    """ Context manager for changing the current working directory """
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
