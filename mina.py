import sublime, sublime_plugin, os, re

class MinaBase(sublime_plugin.TextCommand):
  
  def load_config(self):
    s = sublime.load_settings("mina.sublime-settings")
    global MINA_DEPLOY_CONFIG_DIR; MINA_DEPLOY_CONFIG_DIR = s.get("mina_deploy_config_dir")
    global MINA_DEPLOY_CONFIG_FILE; MINA_DEPLOY_CONFIG_FILE = s.get("mina_deploy_config_file")

  def find_project_dir(self):
    fn = self.view.file_name()
    l = fn.split(os.sep)
    l.pop()
    l.pop(0)
    root = ""
    while len(l):
      pathname = os.sep+os.sep.join(l)
      filename = pathname+os.sep+MINA_DEPLOY_CONFIG_DIR+os.sep+MINA_DEPLOY_CONFIG_FILE
      #print pathname
      if os.path.exists(filename):
        root = pathname
      #print l
      l.pop()
    return root

  def run_shell_command(self, command, working_dir):
    self.view.window().run_command("exec", {
      "cmd": [command],
      "shell": True,
      "working_dir": working_dir
    })

  def error_desc(self,error_id):
    errors = {'no_dir': "Can not find project directory for this file.\nCheck configuration and try again."}
    if error_id in errors:
      return "Mina: "+errors[error_id]
    else:
      return "Mina: "+"Unknown error."

class MinaTask(MinaBase):
  def run_task(self,task):
    self.load_config()
    project_root = self.find_project_dir()
    if not project_root:
      sublime.error_message(self.error_desc("no_dir"))
      return

    match = re.search("configuration", task)
    if match:
      filename = project_root+os.sep+MINA_DEPLOY_CONFIG_DIR+os.sep+MINA_DEPLOY_CONFIG_FILE
      self.view.window().run_command("open_file",{"file":filename})
    else:
      self.run_shell_command(task,project_root)

class MinaTasksCommand(MinaTask):
  def run(self, edit):
    self.run_task("mina tasks")

class MinaDeployCommand(MinaTask):
  def run(self, edit):
    self.run_task("mina deploy")

class MinaSetupCommand(MinaTask):
  def run(self, edit):
    self.run_task("mina setup")

class MinaCleanupCommand(MinaTask):
  def run(self, edit):
    self.run_task("mina cleanup")

class MinaConfigurationCommand(MinaTask):
  def run(self, edit):
    self.run_task("mina configuration")
