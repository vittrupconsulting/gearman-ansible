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
#     proxy.vm.synced_folder ".", "/vagrant"
#     proxy.vm.synced_folder "roles/gearman-proxy", "/etc/ansible/roles/gearman-proxy"
#     proxy.vm.provision "ansible_local" do |ansible|
#       ansible.playbook = "/etc/ansible/roles/gearman-proxy/tests/test.yml"
#     end
   end

   config.vm.define "server" do |server|
     server.vm.network "private_network", ip: "172.16.1.15", virtualbox__intnet: true
#     server.vm.synced_folder ".", "/vagrant"
#     server.vm.synced_folder "roles/gearman-server", "/etc/ansible/roles/gearman-server"
#     server.vm.provision "ansible_local" do |ansible|
#       ansible.playbook = "/etc/ansible/roles/gearman-server/tests/test.yml"
#     end
   end

   config.vm.define "worker" do |worker|
     worker.vm.network "private_network", ip: "172.16.1.20", virtualbox__intnet: true
     worker.vm.synced_folder ".", "/vagrant"
#     worker.vm.provision "shell", inline: <<-SHELL
#       apt-get update
#       sudo apt-get install ansible -y
#       mkdir -p /etc/ansible
#       cp -r /vagrant/roles /etc/ansible/roles
#       ansible-playbook /etc/ansible/roles/gearman-ansible/tests/test.yml
#       ansible-playbook /etc/ansible/roles/gearman-worker/tests/test.yml
#     SHELL
   end

   config.vm.define "utils" do |utils|
     utils.vm.network "private_network", ip: "172.16.1.25", virtualbox__intnet: true
     utils.vm.synced_folder ".", "/vagrant"
     utils.vm.provision "shell", inline: <<-SHELL
       apt-get update
       sudo apt-get install ansible -y
       mkdir -p /etc/ansible

       cp -r /vagrant/roles /etc/ansible/roles
       cp /etc/ansible/roles/gearman-ansible/files/ansible.cfg /etc/ansible/ansible.cfg
       cp /etc/ansible/roles/gearman-ansible/files/ansible_rsa /etc/ansible/ansible_rsa
       chmod 700 /etc/ansible/ansible_rsa

       ansible-playbook --inventory "172.16.1.10," /etc/ansible/roles/gearman-client/tests/test_all.yml
       ansible-playbook --inventory "172.16.1.15," /etc/ansible/roles/gearman-client/tests/test_all.yml
       ansible-playbook --inventory "172.16.1.20," /etc/ansible/roles/gearman-client/tests/test_all.yml
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
