# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
   config.vm.box = "ansible.box"

   config.vm.provision "shell", inline: <<-SHELL
     sudo useradd ansible --system --create-home --shell /bin/bash
     echo 'ansible ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/ansible
     sudo su root --login --command "/usr/bin/mkdir /etc/ansible"
     sudo su root --login --command "/usr/bin/mkdir /etc/ansible/facts.d"
     sudo su root --login --command "/usr/bin/chown -R vagrant:vagrant /etc/ansible"
   SHELL

   config.vm.provision "file", source: "roles", destination: "/etc/ansible/roles"
   config.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
   config.vm.provision "file", source: "ansible_rsa.pub", destination: "/etc/ansible/ansible_rsa.pub"
   config.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
   config.vm.provision "file", source: "common.yml", destination: "/etc/ansible/gearman.yml"

   config.vm.provision "shell", inline: <<-SHELL
     sudo su ansible --login --command "/usr/bin/mkdir /home/ansible/.ssh"
     sudo su ansible --login --command "/usr/bin/cp /etc/ansible/ansible_rsa.pub /home/ansible/.ssh/authorized_keys"
   SHELL

   config.vm.define "gearman-server" do |gearman_server|
     gearman_server.vm.network "private_network", ip: "192.168.0.1", virtualbox__intnet: true
     gearman_server.vm.provision "file", source: "roles/gearman-server/tests/test.yml", destination: "/etc/ansible/common.yml"
     gearman_server.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
#       apt-get update
#       sudo apt-get install ansible -y
       ansible-playbook /etc/ansible/common.yml
     SHELL
   end

   config.vm.define "gearman-proxy" do |gearman_proxy|
     gearman_proxy.vm.network "private_network", ip: "192.168.0.2", virtualbox__intnet: true
     gearman_proxy.vm.network "forwarded_port", guest: 80, host: 80
     gearman_proxy.vm.provision "file", source: "roles/gearman-proxy/tests/test.yml", destination: "/etc/ansible/common.yml"
     gearman_proxy.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-proxy"]' | tee /etc/ansible/facts.d/roles.fact
#       apt-get update
#       sudo apt-get install ansible -y
       ansible-playbook /etc/ansible/common.yml
     SHELL
   end

   config.vm.define "gearman-worker" do |gearman_worker|
     gearman_worker.vm.network "private_network", ip: "192.168.0.3", virtualbox__intnet: true
     gearman_worker.vm.provision "file", source: "roles/gearman-worker/tests/test.yml", destination: "/etc/ansible/common.yml"
     gearman_worker.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
#       apt-get update
#       sudo apt-get install ansible -y
       ansible-playbook /etc/ansible/common.yml
#       ansible-playbook --inventory "192.168.0.1,192.168.0.2,192.168.0.3" /etc/ansible/gearman.yml
     SHELL
   end

   config.vm.define "debian-client", autostart: false do |debian|
     debian.vm.box = "debian/bullseye64"
     debian.vm.network "private_network", ip: "192.168.0.10", virtualbox__intnet: true
     debian.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install gearman-tools -y
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       gearman -h 192.168.0.2 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "ubuntu-client", autostart: false do |ubuntu|
     ubuntu.vm.box = "ubuntu/jammy64"
     ubuntu.vm.network "private_network", ip: "192.168.0.11", virtualbox__intnet: true
     ubuntu.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install gearman-tools -y
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       gearman -h 192.168.0.2 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "alma-client", autostart: false do |alma|
     alma.vm.box = "almalinux/8"
     alma.vm.synced_folder "roles/gearman-common", "/etc/ansible/roles/gearman-common"
     alma.vm.network "private_network", ip: "192.168.0.12", virtualbox__intnet: true
     alma.vm.provision "shell", inline: <<-SHELL
       sudo dnf update -y
       sudo dnf install epel-release -y
       sudo dnf install gearmand -y
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       gearman -h 192.168.0.2 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "centos-client", autostart: false do |centos|
     centos.vm.box = "centos/7"
     centos.vm.network "private_network", ip: "192.168.0.13", virtualbox__intnet: true
     centos.vm.provision "shell", inline: <<-SHELL
       sudo yum update -y
       sudo yum install epel-release -y
       sudo yum install gearmand -y
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       gearman -h 192.168.0.2 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

end
