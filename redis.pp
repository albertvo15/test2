

node 'ubuntu.localdomain' {
#  class { 'redis::install':
#  }

class { 'redis':
  conf_port => '6379',
  conf_bind => '0.0.0.0'

} 
#  redis::server { 'redis-6900':
#    redis_port => '6900',
#    redis_bind_address => '10.20.0.142',
#    redis_password => 'redis_password',
#    redis_max_memory => '1gb',
#  }
}
