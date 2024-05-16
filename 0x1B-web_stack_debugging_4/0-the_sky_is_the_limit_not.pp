# File: nginx_setup.pp

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Executing AB command to test before and after configuration
exec { 'ab_before':
  command     => '/usr/bin/ab -c 100 -n 2000 localhost/',
  logoutput   => true,
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}

# Reload Nginx service after configuration changes
exec { 'nginx_reload':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}

# Executing AB command to test after configuration changes
exec { 'ab_after':
  command     => '/usr/bin/ab -c 100 -n 2000 localhost/',
  logoutput   => true,
  refreshonly => true,
  require     => Exec['nginx_reload'],
}
