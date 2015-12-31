#node default {
# file { '/tmp/hello2':
#   content => 'hello world2\n',
# }
# import 'nodes.pp'
 user { 'carl':
   ensure => present
 }
 file { '/home/carl':
   ensure => directory,
   mode => '0700',
   owner => 'carl',
   require => User["carl"]
 }
 file { '/home/carl/.ssh':
   ensure => directory,
   mode => '0700',
   owner => 'carl',
   require => File["/home/carl"]
 }
 ssh_authorized_key { 'bodl@ubuntu':
   user => 'carl',
   ensure => present,
   type => 'ssh-rsa',
   key => 'AAAAB3NzaC1yc2EAAAADAQABAAABAQC+K3i0DijbvJHsPo/kCmzFl/jGk2h3xgmoWiSWJTDSthEquVwoMDxQwfISIczXoJTc+E9QSwv2AmrWgltNvW7zfLxDcGepuOWqVUmLzKbCUHb26/vopog0Uv/A2MCstmJQVfmNbQiTwFTum+K0KMZF9pe/MrWhyYawbC/qQQPsAGe/f6ISA3LyX0GXktoHavLCIsI4PrGB0NTVVg82somunBaTs7pNuB1PsSDqijsAMhp2r96Mbd4V0XLf5x8M3zizP2EPNYlpZpDGy1SmGMN0t9ZK3WsxDP7zp4dS1PntuO7H+6AKfh1j5VrE3CvYzM2FnDbcuYbJGNE505PQI/YD',
   name => 'bodl@ubuntu',
 }


 user { 'tuserbkc':
   ensure => present,
   home => '/home/tuserbkc',
   shell => '/bin/dash',
 }
 file { '/home/tuserbkc':
   ensure => directory,
   mode => '0700',
   owner => 'tuserbkc',
   require => User["tuserbkc"]
 }
 file { '/home/tuserbkc/.ssh':
   ensure => directory,
   mode => '0700',
   owner => 'tuserbkc',
   require => File["/home/tuserbkc"]
 }
 ssh_authorized_key { 'tuserbkc':
   ensure => 'present',
   user => 'tuserbkc',
   type => 'ssh-dss',
   key => 'AAAAB3NzaC1kc3MAAACBAPgOJm7LqL9rPN3n86+cLcTxzk3BN38CDGgdmJoMKUMGl3dkVFl1ugHFlCqg7cqTSOfypvSO8RSBnDEgWKjlA3q0XQPPMqOc9HN34w16ptnwV2SwLANZZQZoDfjteHqyK3c0XFLDWFHmhIvXhPYjxnr31Lirfrp4sOg6b+NnLMz7AAAAFQDdqT7OtAlxI4eHu8Dp+m4iZh8VqQAAAIEAlkgiDj7ApRqx6e+ZY718iC+jtjee5NUw0ixiorpuTDdtZ3CbJGeC5WoKV/1EyBqdlwbALslXP38+keP1wpmLQXGp2mxi5ksecsKLPGihXrWJiRtWFKMDpka6/J5+xfwoiT36VYeLgDNYDy2oDO70is5B5959SusneeUu3FMv5xMAAACBAMaD0PnHdgBnIoh3Log0bKM8pXA8BYjpmRrdFjhV468LlWGyAc8sEQfSzqQNY07Brg4yZccx/hbo7X10NK34RwpnqY0brOBBkIeUsQgZEgI1tE+awvnTHPb56m6y05UqSmvk3U6aJr52+NWlluL9h3b1wMEokJBiOuz2zS4L3X56',
  name => 'tuser@trulytech.net',
 }
