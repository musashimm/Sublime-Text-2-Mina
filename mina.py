import sublime, sublime_plugin, os

class MinaDeployCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command("exec", { "cmd": 'mina deploy', "shell": True })
      

class MinaTasksCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command("exec", { "cmd": 'mina tasks', "shell": True })


class MinaInitCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command("exec", { "cmd": 'mina init', "shell": True })


class MinaSetupCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command("exec", { "cmd": 'mina setup', "shell": True })


class MinaCleanupCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().run_command("exec", { "cmd": 'mina deploy:cleanup', "shell": True })
