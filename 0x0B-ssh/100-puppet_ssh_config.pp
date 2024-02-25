# Defining the SSH client configuration
file { '/home/anthony/.ssh/config':
   ensure => present,
   owner => 'anthony',
   group => 'anthony',
   mode => '0600',
   content => "
      # SSH client configuration 
      
      Host 47538-web-01
         HostName 3.85.41.151
         User ubuntu
         IdentityFile ~/.ssh/school
         PasswordAuthentication no
      ",
}
