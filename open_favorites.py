# coding=utf8
import sublime, sublime_plugin, re

settings = sublime.load_settings( __name__ + '.sublime-settings')

class open_favoritesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		rp  = settings.get('remove_long_part')
		self.cmds = []
		files = []
		if settings.has('mylist'):
			reg = "^("+"|".join(rp)+")"
			for item in settings.get('mylist'):
				sp = item[1].split('/')
				base_name = sp[len(sp)-1]
				filename = item[1]
				item[1] = re.sub(reg, '', item[1])
				files.append([item[0] + " - "+base_name+"", item[1]])
				self.cmds.append(filename)

		files.append(["Settings", "Configure favorite files"])
		self.cmds.append(sublime.packages_path()+"/MyFavorites/" + __name__ +".sublime-settings")
		self.view.window().show_quick_panel(files, self.mycmd)

	def mycmd(self, list_index):
		try:
			if list_index == -1:
				return
			self.view.window().open_file(self.cmds[list_index])
			sublime.status_message("Opening file: " + self.cmds[list_index])

		except:
			sublime.error_message("Error")
			pass

