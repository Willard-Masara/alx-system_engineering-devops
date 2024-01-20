# automating a 500 status return

$file_to_edit = '/var/www/html/wp-settings.php'

# Replace line containing "phpp" with "php"
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin'],
}

# Manage Apache2 configuration file
file { '/etc/apache2/apache2.conf':
  ensure => file,
  source => 'puppet:///modules/my_module/apache2.conf',
  notify => Service['apache2'],
}

# Manage Apache2 service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/apache2.conf'],
}

