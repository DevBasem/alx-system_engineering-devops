include stdlib
# Setting up my client config file

file_line { 'Turn off passwd auth':
  ensure => present,
  replace => true,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Delare identity file':
  ensure => present,
  replace => true,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
