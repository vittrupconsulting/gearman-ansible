# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ansible.box"

  config.vm.synced_folder "roles", "/etc/ansible/roles"
  config.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
  config.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
  config.vm.provision "file", source: "common.yml", destination: "/etc/ansible/common.yml"
  config.vm.provision "file", source: "generic.yml", destination: "/etc/ansible/generic.yml"
  config.vm.provision "file", source: "inventory.json", destination: "/etc/ansible/inventory.json"
  config.vm.provision "file", source: "environment.ini", destination: "/tmp/environment.ini"

  config.vm.define "server152", autostart: true do |server|
    server.vm.hostname = "server152"
    server.vm.network "private_network", ip: "192.168.0.152", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: "22", host: "49152"
    server.vm.provision "shell", inline: <<-SHELL
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-server"
    SHELL
  end

  config.vm.define "server153", autostart: true do |server|
    server.vm.hostname = "server153"
    server.vm.network "private_network", ip: "192.168.0.153", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: "22", host: "49153"
    server.vm.provision "shell", inline: <<-SHELL
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-server"
    SHELL
  end

  config.vm.define "worker154", autostart: true do |worker|
    worker.vm.hostname = "worker154"
    worker.vm.network "private_network", ip: "192.168.0.154", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: "22", host: "49154"
    worker.vm.provision "shell", inline: <<-SHELL
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-worker"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-ansible"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-etcd"
    SHELL
  end

  config.vm.define "worker155", autostart: true do |worker|
    worker.vm.hostname = "worker155"
    worker.vm.network "private_network", ip: "192.168.0.155", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: "22", host: "49155"
    worker.vm.provision "shell", inline: <<-SHELL
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-worker"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-ansible"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-etcd"
    SHELL
  end

  config.vm.define "worker156", autostart: true do |worker|
    worker.vm.hostname = "worker156"
    worker.vm.network "private_network", ip: "192.168.0.156", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: "22", host: "49156"
    worker.vm.provision "shell", inline: <<-SHELL
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-worker"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-ansible"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-etcd"
    SHELL
  end

  config.vm.define "proxy160", autostart: true do |proxy|
    proxy.vm.hostname = "proxy160"
    proxy.vm.network "private_network", ip: "192.168.0.160", virtualbox__intnet: true
    proxy.vm.network "forwarded_port", guest: "22", host: "49160"
    proxy.vm.network "forwarded_port", guest: "80", host: "80"
    proxy.vm.provision "shell", inline: <<-SHELL
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-proxy"
    SHELL
  end

  config.vm.define "metrics161", autostart: true do |proxy|
    proxy.vm.hostname = "metrics161"
    proxy.vm.network "private_network", ip: "192.168.0.161", virtualbox__intnet: true
    proxy.vm.network "forwarded_port", guest: "22", host: "49161"
    proxy.vm.provision "shell", inline: <<-SHELL
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      cat /tmp/environment.ini | sudo tee -a /etc/hosts
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-metrics"  
    SHELL
  end

  config.vm.define "grafana170", autostart: false do |client|
    client.vm.box = "gearman.box"
    client.vm.hostname = "grafana170"
    client.vm.network "private_network", ip: "192.168.0.170", virtualbox__intnet: true
    client.vm.network "forwarded_port", guest: "22", host: "49170"
    client.vm.network "forwarded_port", guest: "3000", host: "3000"
    client.vm.provision "shell", inline: <<-SHELL
      sudo cp /etc/ansible/roles/gearman-common/files/gearman.py /usr/local/sbin/gearman.py
      sudo chmod 755 /usr/local/sbin/gearman.py
      echo '["192.168.0.160"]' | tee /etc/ansible/facts.d/servers.fact
      /usr/local/sbin/gearman.py `hostname -I | awk '{ print $NF }'`
    SHELL
  end

  config.vm.define "client171", autostart: false do |client|
    client.vm.box = "almalinux.box"
    client.vm.hostname = "client171"
    client.vm.network "private_network", ip: "192.168.0.171", virtualbox__intnet: true
    client.vm.network "forwarded_port", guest: "22", host: "49171"
    client.vm.provision "shell", inline: <<-SHELL
      sudo cp /etc/ansible/roles/gearman-common/files/gearman.py /usr/local/sbin/gearman.py
      sudo chmod 755 /usr/local/sbin/gearman.py
      echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
      echo '["192.168.0.160"]' | tee /etc/ansible/facts.d/servers.fact
      /usr/local/sbin/gearman.py `hostname -I | awk '{ print $NF }'`
    SHELL
  end

  config.vm.define "client172", autostart: false do |client|
    client.vm.box = "centos.box"
    client.vm.hostname = "client172"
    client.vm.network "private_network", ip: "192.168.0.172", virtualbox__intnet: true
    client.vm.network "forwarded_port", guest: "22", host: "49172"
    client.vm.provision "shell", inline: <<-SHELL
      sudo cp /etc/ansible/roles/gearman-common/files/gearman.py /usr/local/sbin/gearman.py
      sudo chmod 755 /usr/local/sbin/gearman.py
      echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
      echo '["192.168.0.160"]' | tee /etc/ansible/facts.d/servers.fact
      /usr/local/sbin/gearman.py `hostname -I | awk '{ print $NF }'`
    SHELL
  end
  
  config.vm.define "galaxy", autostart: false do |init|
    init.vm.provision "shell", inline: <<-SHELL
      mkdir -p /vagrant/roles
      cd /vagrant/roles
      ansible-galaxy init gearman-metrics
    SHELL
  end

end
