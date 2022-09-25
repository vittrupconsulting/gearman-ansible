# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"

   config.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
   end

   config.vm.synced_folder ".", "/vagrant"

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
#        ansible-galaxy init gearman-ansible
#     SHELL
#   end

   config.vm.define "proxy" do |proxy|
     proxy.vm.network "private_network", ip: "172.16.1.10", virtualbox__intnet: true
     proxy.vm.synced_folder "roles/gearman-proxy", "/etc/ansible/roles/gearman-proxy"
     proxy.vm.provision "ansible_local" do |ansible|
       ansible.playbook = "/etc/ansible/roles/gearman-proxy/tests/test.yml"
       ansible.extra_vars = { servers: ["172.16.1.15"] }
     end
   end

   config.vm.define "server" do |server|
     server.vm.network "private_network", ip: "172.16.1.15", virtualbox__intnet: true
     server.vm.synced_folder "roles/gearman-server", "/etc/ansible/roles/gearman-server"
     server.vm.provision "ansible_local" do |ansible|
       ansible.playbook = "/etc/ansible/roles/gearman-server/tests/test.yml"
     end
   end

   config.vm.define "worker" do |worker|
     worker.vm.network "private_network", ip: "172.16.1.20", virtualbox__intnet: true
     worker.vm.synced_folder "roles/gearman-worker", "/etc/ansible/roles/gearman-worker"
     worker.vm.synced_folder "roles/gearman-ansible", "/etc/ansible/roles/gearman-ansible"
     worker.vm.provision "shell", inline: <<-SHELL
       apt-get update
       apt-get install ansible -y
       apt-get install python3-pip -y
     SHELL
     worker.vm.provision "ansible_local" do |ansible|
       ansible.playbook = "/etc/ansible/roles/gearman-worker/tests/test.yml"
       ansible.extra_vars = { servers: ["172.16.1.15"] }
     end
     worker.vm.provision "ansible_local" do |ansible|
       ansible.playbook = "/etc/ansible/roles/gearman-ansible/tests/test.yml"
     end
   end

   config.vm.define "debian", autostart: false do |debian|
     debian.vm.box = "debian/bullseye64"
     debian.vm.network "private_network", ip: "172.16.1.30", virtualbox__intnet: true
     debian.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install gearman-tools -y
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "ubuntu", autostart: false do |ubuntu|
     ubuntu.vm.box = "ubuntu/jammy64"
     ubuntu.vm.network "private_network", ip: "172.16.1.31", virtualbox__intnet: true
     ubuntu.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install gearman-tools -y
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "alma8", autostart: false do |alma8|
     alma8.vm.box = "almalinux/8"
     alma8.vm.network "private_network", ip: "172.16.1.32", virtualbox__intnet: true
     alma8.vm.provision "shell", inline: <<-SHELL
       sudo dnf update -y
       sudo dnf install epel-release -y
       sudo dnf update -y
       sudo dnf install gearmand -y
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "alma9", autostart: false do |alma9|
     alma9.vm.box = "almalinux/9"
     alma9.vm.network "private_network", ip: "172.16.1.33", virtualbox__intnet: true
     alma9.vm.provision "shell", inline: <<-SHELL
       sudo dnf update -y
       sudo dnf install epel-release -y
       sudo dnf update -y
       sudo dnf install gearmand -y
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "centos7", autostart: false do |centos7|
     centos7.vm.box = "centos/7"
     centos7.vm.network "private_network", ip: "172.16.1.34", virtualbox__intnet: true
     centos7.vm.provision "shell", inline: <<-SHELL
       yum update -y
     SHELL
   end

   config.vm.define "centos8", autostart: false do |centos8|
     centos8.vm.box = "centos/8"
     centos8.vm.network "private_network", ip: "172.16.1.35", virtualbox__intnet: true
     centos8.vm.provision "shell", inline: <<-SHELL
       yum update -y
     SHELL
   end

   config.vm.define "rocky8", autostart: false do |rocky8|
     rocky8.vm.box = "rockylinux/8"
     rocky8.vm.network "private_network", ip: "172.16.1.36", virtualbox__intnet: true
     rocky8.vm.provision "shell", inline: <<-SHELL
       yum update -y
     SHELL
   end

end
