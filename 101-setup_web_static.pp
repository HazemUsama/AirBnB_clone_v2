# Redo task 0 with Puppet

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create directories
file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { [
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/',
]:
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Service definition for Nginx
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}


