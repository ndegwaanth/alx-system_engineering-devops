# Define class to configure custom HTTP response header
class nginx_custom_header {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is running and enabled
  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  # Create custom 404 error page
  file { '/usr/share/nginx/html/custom_404.html':
    ensure  => present,
    content => '404 - Not Found',
  }

  # Add custom response header to Nginx configuration
  file_line { 'custom_http_header':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => '  add_header X-Served-By $hostname;',
    require => Package['nginx'],
  }

  # Configure Nginx to use custom 404 error page
  file_line { 'custom_404_error_page':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => '  error_page 404 /custom_404.html;',
    require => File['/usr/share/nginx/html/custom_404.html'],
  }

  # Restart Nginx service to apply changes
  exec { 'nginx_reload':
    command     => 'systemctl restart nginx',
    refreshonly => true,
    subscribe   => [File_line['custom_http_header'], File_line['custom_404_error_page']],
  }
}

# Apply the class to all nodes
include nginx_custom_header
