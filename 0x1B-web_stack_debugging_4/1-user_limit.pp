# File: 1-user_limit.pp

# Ensure the file /etc/security/limits.conf exists
file { '/etc/security/limits.conf':
  ensure => present,
}

# Add configuration to increase the file descriptor limit for the holberton user
file_line { 'holberton_file_limit':
  ensure  => present,
  path    => '/etc/security/limits.conf',
  line    => '*               hard    nofile          65535',
  match   => '^*.*nofile',
}

# Executing command to apply the new limits without a reboot
exec { 'apply_limits':
  command => 'sysctl -p',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin',
  onlyif  => 'test -f /etc/security/limits.conf',
}

# Ensure the changes take effect immediately
exec { 'reload_limits':
  command     => 'ulimit -n 65535',
  path        => '/bin:/sbin:/usr/bin:/usr/sbin',
  refreshonly => true,
  subscribe   => File_line['holberton_file_limit'],
}

# Notify the user when the configuration is applied
notify { 'Configuration_applied':
  message => 'File descriptor limit increased for the holberton user.',
}
