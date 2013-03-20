import sublime
import sublime_plugin
import os
import re


class MinaBase(sublime_plugin.TextCommand):

    def load_config(self):
        s = sublime.load_settings("mina.sublime-settings")
        return [s.get("mina_deploy_config_dir"), s.get("mina_deploy_config_file")]

    def find_project_dir(self, deploy_dir, deploy_file):
        fn = self.view.file_name()
        print fn
        l = fn.split(os.sep)
        l.pop()
        l.pop(0)
        root = ""
        while len(l):
            pathname = os.sep + os.sep.join(l)
            filename = pathname + os.sep + deploy_dir + os.sep + deploy_file
            #print pathname
            if os.path.exists(filename):
                root = pathname
            #print l
            l.pop()
        return root

    def run_shell_command(self, command, working_dir):
        self.panel = self.view.window().get_output_panel("exec")
        self.panel.settings().set("syntax", "Packages/Mina/MinaConsole.tmLanguage")
        self.panel.settings().set("color_scheme", "Packages/Mina/MinaConsole.tmTheme")
        self.view.window().run_command("exec", {
            "cmd": [command],
            "shell": True,
            "working_dir": working_dir
        })

    def error_desc(self, error_id):
        errors = {'no_dir': "Can not find project directory for this file.\nCheck configuration and try again."}
        if error_id in errors:
            return "Mina: " + errors[error_id]
        else:
            return "Mina: " + "Unknown error."


class MinaTask(MinaBase):
    def run_task(self, task):
        deploy_dir, deploy_file = self.load_config()
        project_root = self.find_project_dir(deploy_dir, deploy_file)
        if not project_root:
            sublime.error_message(self.error_desc("no_dir"))
            return
        match = re.search("configuration", task)
        if match:
            filename = project_root + os.sep + deploy_dir + os.sep + deploy_file
            print filename
            self.view.window().run_command("open_file", {"file": filename})
        else:
            self.run_shell_command(task, project_root)


class MinaTasksCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina tasks")

class MinaRestartCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina restart")

class MinaDeployCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina deploy")

class MinaSetupCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina setup")

class MinaCleanupCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina deploy:cleanup")

class MinaConfigurationCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina configuration")

# Custom tasks

class MinaCustomAssetsCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina custom_assets")

class MinaCustomConfigCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina custom_config")

class MinaCustomSyncCommand(MinaTask):
    def run(self, edit):
        self.run_task("mina custom_sync")

