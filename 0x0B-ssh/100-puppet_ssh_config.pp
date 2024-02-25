# 100-puppet_ssh_config.pp

class { 'stdlib': }

# Ensure SSH client configuration
include stdlib

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

# Notify SSH service to reload configuration
service { 'ssh':
  ensure    => running,
  enable    => true,
  subscribe => File_line['Turn off passwd auth', 'Declare identity file'],
}
