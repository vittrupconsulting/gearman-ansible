# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"

   config.vm.provider "virtualbox" do |vb|
     vb.memory = "2048"
   end

#    config.vm.define "init", autostart: false do |init|
#      init.vm.synced_folder ".", "/vagrant"
#      init.vm.provision "shell", inline: <<-SHELL
#        apt-get update
#        apt-get install ansible -y
#        mkdir -p /vagrant/roles
#        cd /vagrant/roles
#        ansible-galaxy init gearman-server
#        ansible-galaxy init gearman-worker
#        ansible-galaxy init gearman-proxy
#        ansible-galaxy init gearman-client
#      SHELL
#    end

   config.vm.define "server" do |server|
     server.vm.network "private_network", ip: "172.16.1.10", virtualbox__intnet: true
     server.vm.synced_folder "roles/gearman-server", "/etc/ansible/roles/gearman-server"
     server.vm.provision "shell", inline: <<-SHELL
       apt-get update
       apt-get install ansible -y
       sudo ansible-playbook /etc/ansible/roles/gearman-server/tests/test.yml
     SHELL
   end

   config.vm.define "proxy" do |proxy|
     proxy.vm.network "private_network", ip: "172.16.1.15", virtualbox__intnet: true
     proxy.vm.network "forwarded_port", guest: 4730, host: 4730
     proxy.vm.synced_folder "roles/gearman-proxy", "/etc/ansible/roles/gearman-proxy"
     proxy.vm.provision "shell", inline: <<-SHELL
       apt-get update
       apt-get install ansible -y
	   sudo ansible-playbook /etc/ansible/roles/gearman-proxy/tests/test.yml
     SHELL
   end

   config.vm.define "worker" do |worker|
     worker.vm.network "private_network", ip: "172.16.1.20", virtualbox__intnet: true
     worker.vm.synced_folder "roles/gearman-worker", "/etc/ansible/roles/gearman-worker"
     worker.vm.provision "shell", inline: <<-SHELL
       apt-get update
       apt-get install ansible -y
	   sudo ansible-playbook /etc/ansible/roles/gearman-worker/tests/test.yml
     SHELL
   end

   config.vm.define "debian-client", autostart: false  do |debian|
     debian.vm.network "private_network", ip: "172.16.1.30", virtualbox__intnet: true
     debian.vm.synced_folder "roles/gearman-client", "/etc/ansible/roles/gearman-client"
     debian.vm.provision "shell", inline: <<-SHELL
       apt-get update
       apt-get install ansible -y
	   sudo ansible-playbook /etc/ansible/roles/gearman-client/tests/test.yml
       sudo apt-get install python3-pip -y
       sudo pip3 install gear
	   python3 /opt/client.py `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "alma-client", autostart: false  do |alma|
     alma.vm.box = "almalinux/8"
     alma.vm.synced_folder "roles/gearman-client", "/etc/ansible/roles/gearman-client"
     alma.vm.network "private_network", ip: "172.16.1.31", virtualbox__intnet: true
     alma.vm.provision "shell", inline: <<-SHELL
       yum update
       yum install ansible-core -y
	   sudo ansible-playbook /etc/ansible/roles/gearman-client/tests/test.yml
	   python3 /opt/client.py `hostname -I | awk '{ print $NF }'`
#       sudo pip3 install gear
#       sudo cp /data/roles/gearman-worker/files/client.py /opt/gearman.py
#       python3 /opt/gearman.py `hostname -I | awk '{ print $NF }'`
     SHELL
   end

end
