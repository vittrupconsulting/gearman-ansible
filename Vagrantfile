# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "gearman.box"

  config.vm.provision "shell", inline: <<-SHELL
    echo "192.168.0.152 server152" | sudo tee -a /etc/hosts
    echo "192.168.0.153 server153" | sudo tee -a /etc/hosts
    echo "192.168.0.154 inventory154" | sudo tee -a /etc/hosts
    echo "192.168.0.155 inventory155" | sudo tee -a /etc/hosts
    echo "192.168.0.156 inventory156" | sudo tee -a /etc/hosts
    echo "192.168.0.157 ansible157" | sudo tee -a /etc/hosts
    echo "192.168.0.158 ansible158" | sudo tee -a /etc/hosts
    echo "192.168.0.160 proxy160" | sudo tee -a /etc/hosts
    echo "192.168.0.161 metrics161" | sudo tee -a /etc/hosts
    echo "192.168.0.170 grafana170" | sudo tee -a /etc/hosts
    echo "192.168.0.200 ansible200" | sudo tee -a /etc/hosts
  SHELL

  (152..153).each do |i|
    config.vm.define "server#{i}", autostart: true do |server|
      server.vm.hostname = "server#{i}"
      server.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
    end
  end

  (154..156).each do |i|
    config.vm.define "inventory#{i}", autostart: true do |inventory|
      inventory.vm.hostname = "inventory#{i}"
      inventory.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
    end
  end

  (157..158).each do |i|
    config.vm.define "ansible#{i}", autostart: true do |ansible|
      ansible.vm.hostname = "ansible#{i}"
      ansible.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
    end
  end

  (160..160).each do |i|
    config.vm.define "proxy#{i}", autostart: true do |proxy|
      proxy.vm.hostname = "proxy#{i}"
      proxy.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
      proxy.vm.network "forwarded_port", guest: "80", host: "80"
    end
  end

  (161..161).each do |i|
  config.vm.define "metrics#{i}", autostart: true do |metrics|
      metrics.vm.hostname = "metrics#{i}"
      metrics.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
    end
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

#   config.vm.define "galaxy", autostart: false do |init|
#     init.vm.provision "shell", inline: <<-SHELL
#       mkdir -p /vagrant/roles
#       cd /vagrant/roles
#       ansible-galaxy init gearman-metrics
#     SHELL
#   end

  config.vm.define "ansible200", autostart: true do |server|
    server.vm.box = "ansible.box"
    server.vm.hostname = "ansible200"
    server.vm.network "private_network", ip: "192.168.0.200", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: "22", host: "49200"
    server.vm.synced_folder "roles", "/etc/ansible/roles"
    server.vm.synced_folder "inventory", "/etc/ansible/inventory"
    server.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
    server.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
    server.vm.provision "file", source: "generic.yml", destination: "/etc/ansible/generic.yml"
    server.vm.provision "shell", inline: <<-SHELL
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-common"
      ansible-playbook --inventory "localhost," /etc/ansible/generic.yml -e "role=gearman-ansible"
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" /etc/ansible/generic.yml --extra-vars "role=gearman-common"
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-common" /etc/ansible/generic.yml
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-server" -l "gearman-server" /etc/ansible/generic.yml
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-etcd" -l "gearman-etcd" /etc/ansible/generic.yml
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-ansible" -l "gearman-ansible" /etc/ansible/generic.yml
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-worker" -l "gearman-worker" /etc/ansible/generic.yml
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-proxy" -l "gearman-proxy" /etc/ansible/generic.yml
      ansible-playbook -i "/etc/ansible/inventory/inventory.yml" -e "role=gearman-metrics" -l "gearman-metrics" /etc/ansible/generic.yml
    SHELL
  end

end
