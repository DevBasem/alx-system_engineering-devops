# Puppet manifest to fix bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

# Use package resource to ensure Apache is installed
package { 'apache2':
  ensure => installed,
}

# Define service resource for Apache
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}

# Define file resource to fix the typo in wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template("<%= File.read('/var/www/html/wp-settings.php').gsub('phpp', 'php') %>"),
  require => Package['apache2'], # Correct dependency declaration
  notify  => Service['apache2'],
}
