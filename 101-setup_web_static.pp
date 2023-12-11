
package { 'nginx':
  ensure    => 'installed',
}

file { '/data/web_static/shared/':
  ensure    => 'directory',
}

file { '/data/web_static/releases/test/':
  ensure    => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
}

file { '/data/web_static/current/':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => true,
}

file { '/data/':
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
