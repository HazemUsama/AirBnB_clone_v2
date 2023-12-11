# Puppet to redo task 0

# Install Nginx
package { 'ngix':
  ensure => installed,
}

# Create Directory & Files

file { [
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/',
]:
  ensure  => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
