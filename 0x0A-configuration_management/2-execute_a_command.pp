#!/usr/bin/pup
#This manifest uses exec resourse to kill a process
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
}

