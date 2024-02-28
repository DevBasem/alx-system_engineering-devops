# Puppet Manifest for Installing and Configuring NginX

# Update package lists
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

# Install NginX package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

# Create a basic HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure redirection for specific URL
exec {'redirect_me_config':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

# Ensure NginX service is running
service { 'nginx':
  ensure  => running,
  require => [Package['nginx'], Exec['redirect_me_config']],
}