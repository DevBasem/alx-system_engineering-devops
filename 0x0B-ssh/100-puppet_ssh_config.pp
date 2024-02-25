# 100-puppet_ssh_config.pp

# Install puppetlabs/stdlib module
class { 'stdlib': }

# Ensure SSH client configuration
include stdlib

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

# Notify SSH service to reload configuration
service { 'ssh':
  ensure    => running,
  enable    => true,
  subscribe => File_line['Turn off passwd auth', 'Declare identity file'],
}