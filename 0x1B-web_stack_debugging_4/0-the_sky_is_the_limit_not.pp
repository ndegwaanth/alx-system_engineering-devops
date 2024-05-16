# fix request dropping in nginx

exec { 'increase ulimit':
  path    => '/bin',
  command => "sed -i 's/15/2000/g' /etc/default/nginx"
}

exec { 'nginx restart':
  path    => '/usr/sbin',
  command => 'service nginx restart'
}
