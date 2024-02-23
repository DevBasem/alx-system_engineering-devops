# Puppet manifest to kill a process named killmenow

exec { 'kill_killmenow_process':
  command  => 'pkill killmenow',
  provider => 'shell',
}