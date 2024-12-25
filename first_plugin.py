import sublime
import sublime_plugin

class MyPluginCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		content = self.get_characters_html()
		self.view.show_popup(content, flags=sublime.HTML, location=-1, max_width=1000, max_height=1000, on_navigate=self.on_choice_symbol)

	def get_characters_html(self):
		resources = sublime.find_resources('my_unicodes.html')
		content = sublime.load_resource(resources[0])
		return content

	def on_choice_symbol(self, symbol):
		self.view.run_command("insert", {"characters": symbol})
		self.view.hide_popup()