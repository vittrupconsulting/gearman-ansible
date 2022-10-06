# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ansible.box"

  #config.vm.provision "file", source: "roles", destination: "/etc/ansible/roles"
  config.vm.synced_folder "roles", "/etc/ansible/roles"
  config.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
  config.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
  config.vm.provision "file", source: "common.yml", destination: "/etc/ansible/common.yml"

# (152..153).each do |i|
#   config.vm.define "server-#{i}" do |server|
#     server.vm.hostname = "server-#{i}.localhost"
#     server.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
#     server.vm.network "forwarded_port", guest: "22", host: "49#{i}"
#     server.vm.provision "shell", inline: <<-SHELL
#       echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
#       ansible-playbook --inventory "localhost," /etc/ansible/common.yml
#     SHELL
#   end
# end

  config.vm.define "server-152", autostart: true do |server|
    server.vm.hostname = "server-152.localhost"
    server.vm.network "private_network", ip: "192.168.0.152", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: "22", host: "49152"
    server.vm.provision "shell", inline: <<-SHELL
      echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
      ansible-playbook --inventory "localhost," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "server-153", autostart: false do |server|
    server.vm.hostname = "server-153.localhost"
    server.vm.network "private_network", ip: "192.168.0.153", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: "22", host: "49153"
    server.vm.provision "shell", inline: <<-SHELL
      echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
      ansible-playbook --inventory "localhost," /etc/ansible/common.yml
    SHELL
  end

# (154..155).each do |i|
#   config.vm.define "worker-#{i}" do |worker|
#     worker.vm.hostname = "worker-#{i}.localhost"
#     worker.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
#     worker.vm.network "forwarded_port", guest: "22", host: "49#{i}"
#     worker.vm.provision "shell", inline: <<-SHELL
#       echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
#       echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
#       ansible-playbook --inventory "localhost," /etc/ansible/common.yml
#     SHELL
#   end
# end

  config.vm.define "worker-154", autostart: true do |worker|
    worker.vm.hostname = "worker-154.localhost"
    worker.vm.network "private_network", ip: "192.168.0.154", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: "22", host: "49154"
    worker.vm.provision "shell", inline: <<-SHELL
      echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      ansible-playbook --inventory "localhost," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "worker-155", autostart: false do |worker|
    worker.vm.hostname = "worker-155.localhost"
    worker.vm.network "private_network", ip: "192.168.0.155", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: "22", host: "49155"
    worker.vm.provision "shell", inline: <<-SHELL
      echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      ansible-playbook --inventory "localhost," /etc/ansible/common.yml
    SHELL
  end
  
  config.vm.define "proxy-160", autostart: false do |proxy|
    proxy.vm.hostname = "proxy-160.localhost"
    proxy.vm.network "private_network", ip: "192.168.0.160", virtualbox__intnet: true
    proxy.vm.network "forwarded_port", guest: 22, host: 49160
    proxy.vm.network "forwarded_port", guest: 80, host: 80
    proxy.vm.provision "shell", inline: <<-SHELL
      echo '["gearman-common", "gearman-proxy"]' | tee /etc/ansible/facts.d/roles.fact
      echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
      ansible-playbook --inventory "localhost," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "client-170", autostart: true do |client|
    client.vm.box = "gearman.box"
    client.vm.hostname = "client-170.localhost"
    client.vm.network "private_network", ip: "192.168.0.170", virtualbox__intnet: true
    client.vm.network "forwarded_port", guest: "22", host: "49170"
    client.vm.provision "shell", inline: <<-SHELL
      sudo cp /etc/ansible/roles/gearman-common/files/gearman.py /usr/local/sbin/gearman.py
      sudo chmod 755 /usr/local/sbin/gearman.py
      echo '["gearman-common", "grafana-server", "grafana-config"]' | sudo tee /etc/ansible/facts.d/roles.fact
      echo '["192.168.0.152"]' | tee /etc/ansible/facts.d/servers.fact
      /usr/local/sbin/gearman.py `hostname -I | awk '{ print $NF }'`
    SHELL
  end

  config.vm.define "client-171", autostart: false do |client|
    client.vm.box = "almalinux.box"
    client.vm.hostname = "client-171.localhost"
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

  config.vm.define "client-172", autostart: false do |client|
    client.vm.box = "centos.box"
    client.vm.hostname = "client-172.localhost"
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
      ansible-galaxy init XXX
    SHELL
  end

end
