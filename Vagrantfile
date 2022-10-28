# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/debian11"

  config.vm.provider "vmware_desktop" do |vmware|
    vmware.vmx["memsize"] = "512"
    vmware.vmx["numvcpus"] = "1"
    vmware.vmx["ethernet0.pcislotnumber"] = "32"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo useradd ansible --system --create-home --shell /bin/bash
    echo 'ansible ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/ansible
    sudo su root --login --command "/usr/bin/mkdir /etc/ansible"
    sudo su root --login --command "/usr/bin/mkdir /etc/ansible/facts.d"
    sudo su ansible --login --command "/usr/bin/mkdir /home/ansible/.ssh"
    sudo su ansible --login --command "/usr/bin/echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDO/b4LqHoJPSWLovBmo8jaj9RWNmtdSyoUJVd/0lnGQpTOgKhM6GA4K+sNIKSjZSRqVmp0qvYxNhMSGnnDzagsZY9ydfF0R5/2SAFI7ezn+z75LbyAx0vpk7e4KIxPatx7/YAABQMOa9dT/qPhSXJ9/YO4QYPFUA3AyMQLJwb5Am6jlqxYBpRe+zt8HUlat2HD628YBNKWyqSsL13kKt2QzaAHT75ZqPEHlQMA3Q/kjmAW4McqtQ6BhVwhGaneslbsj8A/fQGzxRQtW81MC7K83x7RSwV40NXcJeUEYcJyhD029dg74wA875Vv9S7Y4MF+OKO2w4bRm+1uyTIXSAhIsVWbB3uyoFz2EjfMEsSK6uqMGbbGyC7pTXz1qkX0tPWkkLvUTbjIs2FDCE+eWOI/neQ32jdMBsZujzJ8i4VdQeGUUfJATuRB6hjm1XEVx0wzRfNAGba2OxCjj9dx5URgVje55+POxDPPfpCaAL98/xCZmuP/SgYk44YIEqFXtXc=' | tee /home/ansible/.ssh/authorized_keys"
    cat  /vagrant/misc/hosts | sudo tee -a /etc/hosts
  SHELL

  config.vm.define "server52", autostart: true do |server|
    server.vm.hostname = "server52"
    server.vm.base_address = "192.168.147.52"
    server.vm.base_mac = "00:50:56:33:C5:20"
    server.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.52"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "server53", autostart: true do |server|
    server.vm.hostname = "server53"
    server.vm.base_address = "192.168.147.53"
    server.vm.base_mac = "00:50:56:26:59:69"
    server.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.53"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "inventory54", autostart: true do |inventory|
    inventory.vm.hostname = "inventory54"
    inventory.vm.base_address = "192.168.147.54"
    inventory.vm.base_mac = "00:50:56:2D:BF:4B"
    inventory.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.54"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "inventory55", autostart: true do |inventory|
    inventory.vm.hostname = "inventory55"
    inventory.vm.base_address = "192.168.147.55"
    inventory.vm.base_mac = "00:50:56:25:6B:47"
    inventory.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.55"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "inventory56", autostart: true do |inventory|
    inventory.vm.hostname = "inventory56"
    inventory.vm.base_address = "192.168.147.56"
    inventory.vm.base_mac = "00:50:56:31:F2:39"
    inventory.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.56"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "ansible57", autostart: true do |ansible|
    ansible.vm.hostname = "ansible57"
    ansible.vm.base_address = "192.168.147.57"
    ansible.vm.base_mac = "00:50:56:22:A6:4D"
    ansible.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.57"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "ansible58", autostart: true do |ansible|
    ansible.vm.box = "generic/centos9s"
    ansible.vm.hostname = "ansible58"
    ansible.vm.base_address = "192.168.147.58"
    ansible.vm.base_mac = "00:50:56:2D:FF:49"
    ansible.vm.provision "shell", inline: <<-SHELL
      sudo dnf install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.58"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "proxy60", autostart: true do |proxy|
    proxy.vm.hostname = "proxy60"
    proxy.vm.base_address = "192.168.147.60"
    proxy.vm.network "forwarded_port", guest: "80", host: "80"
    proxy.vm.base_mac = "00:50:56:3B:2A:37"
    proxy.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.60"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "metrics61", autostart: true do |metrics|
    metrics.vm.hostname = "metrics61"
    metrics.vm.base_address = "192.168.147.61"
    metrics.vm.base_mac = "00:50:56:33:E6:D0"
    metrics.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.61"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "grafana70", autostart: true do |grafana|
    grafana.vm.hostname = "grafana70"
    grafana.vm.base_address = "192.168.147.70"
    grafana.vm.network "forwarded_port", guest: "3000", host: "3000"
    grafana.vm.base_mac = "00:50:56:39:02:0C"
    grafana.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear
	  echo '{"address": "192.168.147.70"}' | jq . | sudo tee /etc/ansible/facts.d/settings.fact
    SHELL
  end

  config.vm.define "jumphost", autostart: true do |server|
    server.vm.hostname = "jumphost"
    server.vm.base_address = "192.168.147.80"
    server.vm.base_mac = "00:50:56:2B:E7:26"
    server.vm.network "forwarded_port", guest: "22", host: "49152"
    server.vm.synced_folder ".", "/vagrant"
    server.vm.provision "shell", inline: <<-SHELL
      apt-get update
      sudo apt-get install python3-pip nmap curl jq -y
      sudo pip install gear

      sudo chown ansible:ansible /etc/ansible
      sudo su ansible --login --command "cp -r /vagrant/* /etc/ansible/"
      sudo su ansible --login --command "chmod 600 /etc/ansible/ansible_rsa"
      pip install ansible

      echo '#!/bin/bash' | tee /home/ansible/init.sh
      echo 'ansible-playbook -i "/etc/ansible/bootstrap.yml" /etc/ansible/generic.yml' | tee -a /home/ansible/init.sh
      chmod +x /home/ansible/init.sh
    SHELL
  end
end
