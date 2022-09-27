# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"

   config.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
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
#        ansible-galaxy init gearman-ansible
#     SHELL
#   end

   config.vm.provision "shell", inline: <<-SHELL
     echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
   SHELL

   config.vm.define "proxy" do |proxy|
     proxy.vm.network "private_network", ip: "172.16.1.10", virtualbox__intnet: true
     proxy.vm.network "forwarded_port", guest: 80, host: 80
     proxy.vm.provision "shell", inline: <<-SHELL
        sudo mkdir -p /etc/ansible/facts.d/
        echo '["gearman-client", "gearman-proxy"]' | sudo tee /etc/ansible/facts.d/roles.fact
     SHELL
   end

   config.vm.define "server1" do |server1|
     server1.vm.network "private_network", ip: "172.16.1.15", virtualbox__intnet: true
     server1.vm.provision "shell", inline: <<-SHELL
        sudo mkdir -p /etc/ansible/facts.d/
        echo '["gearman-client", "gearman-server"]' | sudo tee /etc/ansible/facts.d/roles.fact
     SHELL
   end

   config.vm.define "server2" do |server2|
     server2.vm.network "private_network", ip: "172.16.1.16", virtualbox__intnet: true
     server2.vm.provision "shell", inline: <<-SHELL
        sudo mkdir -p /etc/ansible/facts.d/
        echo '["gearman-client", "gearman-server"]' | sudo tee /etc/ansible/facts.d/roles.fact
     SHELL
   end

   config.vm.define "worker1" do |worker1|
     worker1.vm.network "private_network", ip: "172.16.1.20", virtualbox__intnet: true
     worker1.vm.provision "shell", inline: <<-SHELL
        sudo mkdir -p /etc/ansible/facts.d/
        echo '["gearman-client", "gearman-ansible", "gearman-worker"]' | sudo tee /etc/ansible/facts.d/roles.fact
     SHELL
   end

   config.vm.define "worker2" do |worker2|
     worker2.vm.network "private_network", ip: "172.16.1.21", virtualbox__intnet: true
     worker2.vm.provision "shell", inline: <<-SHELL
        sudo mkdir -p /etc/ansible/facts.d/
        echo '["gearman-client", "gearman-ansible", "gearman-worker"]' | sudo tee /etc/ansible/facts.d/roles.fact
     SHELL
   end

   config.vm.define "utils" do |utils|
     utils.vm.network "private_network", ip: "172.16.1.25", virtualbox__intnet: true
     utils.vm.synced_folder ".", "/vagrant"
     utils.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install ansible -y
       mkdir -p /etc/ansible

       cp -r /vagrant/* /etc/ansible
       sudo rm -f /etc/ansible/Vagrantfile
       sudo chmod 700 /etc/ansible/ansible_rsa
       sudo chown -R vagrant:vagrant /etc/ansible

       ansible-playbook --inventory "172.16.1.10," /etc/ansible/common.yml
       ansible-playbook --inventory "172.16.1.15," /etc/ansible/common.yml
       ansible-playbook --inventory "172.16.1.16," /etc/ansible/common.yml
       ansible-playbook --inventory "172.16.1.20," /etc/ansible/common.yml
       ansible-playbook --inventory "172.16.1.21," /etc/ansible/common.yml
     SHELL
   end

   config.vm.define "debian-client", autostart: false do |debian|
     debian.vm.box = "debian/bullseye64"
     debian.vm.network "private_network", ip: "172.16.1.30", virtualbox__intnet: true
     debian.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install gearman-tools -y
       echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "ubuntu-client", autostart: false do |ubuntu|
     ubuntu.vm.box = "ubuntu/jammy64"
     ubuntu.vm.network "private_network", ip: "172.16.1.31", virtualbox__intnet: true
     ubuntu.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install gearman-tools -y
       echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "alma-client", autostart: false do |alma|
     alma.vm.box = "almalinux/8"
     alma.vm.synced_folder "roles/gearman-client", "/etc/ansible/roles/gearman-client"
     alma.vm.network "private_network", ip: "172.16.1.32", virtualbox__intnet: true
     alma.vm.provision "shell", inline: <<-SHELL
       sudo dnf update -y
       sudo dnf install epel-release -y
       sudo dnf install gearmand -y
       echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

   config.vm.define "centos-client", autostart: false do |centos|
     centos.vm.box = "centos/7"
     centos.vm.network "private_network", ip: "172.16.1.33", virtualbox__intnet: true
     centos.vm.provision "shell", inline: <<-SHELL
       sudo yum update -y
       sudo yum install epel-release -y
       sudo yum install gearmand -y
       echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
       gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
     SHELL
   end

#    config.vm.define "rocky-client", autostart: false do |rocky|
#      rocky.vm.box = "rockylinux/8"
#      rocky.vm.network "private_network", ip: "172.16.1.34", virtualbox__intnet: true
#      rocky.vm.provision "shell", inline: <<-SHELL
#        sudo dnf update -y
#        sudo dnf install epel-release -y
#        sudo dnf install gearmand -y
#        echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
#        gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
#      SHELL
#    end

#    config.vm.define "python-client", autostart: false do |python|
#      python.vm.box = "debian/bullseye64"
#      python.vm.synced_folder "roles/gearman-client", "/etc/ansible/roles/gearman-client"
#      python.vm.network "private_network", ip: "172.16.1.35", virtualbox__intnet: true
#      python.vm.provision "shell", inline: <<-SHELL
#        sudo apt-get update
#        sudo apt-get install python3 python3-pip -y
#        sudo pip3 install gear
#        sudo cp /etc/ansible/roles/gearman-client/files/client.py /usr/bin/gearman
#        echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=" >> /home/vagrant/.ssh/authorized_keys
#        gearman -h 172.16.1.10 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`(python)
#      SHELL
#    end

end
