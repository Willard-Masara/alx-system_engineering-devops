# 0-strace_is_your_friend.pp

file { '/etc/apache2/apache2.conf':
  ensure => file,
  source => 'puppet:///modules/my_module/apache2.conf',
  notify => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/apache2.conf'],
}

