#!/usr/bin/pup
#This script demonstates use of package in puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

