# Puppet manifest to install Flask version 2.1.0 with specific Werkzeug version using pip3

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}