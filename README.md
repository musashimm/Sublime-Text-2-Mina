Sublime-Text-2-Mina
===================

Overview
--------

Sublime-Text-2-Mina is a plugin for [Mina](http://nadarei.co/mina/) gem deployment tool for Sublime editor. It adds to Tool menu and to command palette some Mina commands.

![screenshot](https://raw.github.com/musashimm/Sublime-Text-2-Mina/master/screenshot.png "screenshot")

Installation
------------

Clone repository to Your Sublime Package directory or use [Sublime Packege Control ](http://wbond.net/sublime_packages/package_control).

Custom tasks
------------

To use custom task you must define them like so:

```ruby
desc "Custom Assets."
task :custom_assets do
  system "scp my_assets/* #{deploy_to}/#{current_path}/assets/"
end
```

Custom assets are helpful for example to override some configuration or specific files.

Specic config
-------------

In _deploy.rb_ file use:

```ruby
set :term_mode, nil
```

to have cleaner panel output.
