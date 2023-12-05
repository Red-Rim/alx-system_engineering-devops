#add ......
exec { 'configure-nginx':
  command     => 'apt-get update && apt-get install -y nginx',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('path/to/nginx_config_template.erb'),
  notify  => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command     => 'service nginx restart',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

