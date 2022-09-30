# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ansible.box"

  config.vm.provision "file", source: "roles", destination: "/etc/ansible/roles"
  config.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
  config.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
  config.vm.provision "file", source: "common.yml", destination: "/etc/ansible/common.yml"

  config.vm.define "proxy" do |proxy|
    proxy.vm.network "private_network", ip: "192.168.0.152", virtualbox__intnet: true
    proxy.vm.network "forwarded_port", guest: 22, host: 49152
    proxy.vm.network "forwarded_port", guest: 80, host: 80
    proxy.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-proxy"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.152," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "server" do |server|
    server.vm.network "private_network", ip: "192.168.0.153", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: 22, host: 49153
    server.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.153," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "worker" do |worker|
    worker.vm.network "private_network", ip: "192.168.0.154", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: 22, host: 49154
    worker.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.154," /etc/ansible/common.yml
    SHELL
  end

  config.vm.define "client", autostart: false do |client|
    client.vm.box = "gearman.box"
    client.vm.network "private_network", ip: "192.168.0.155", virtualbox__intnet: true
    client.vm.network "forwarded_port", guest: 22, host: 49155
    client.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       gearman -h 192.168.0.152 -p 4730 -f ansible `hostname -I | awk '{ print $NF }'`
    SHELL
  end

  config.vm.define "galaxy", autostart: false do |init|
    init.vm.provision "shell", inline: <<-SHELL
      mkdir -p /vagrant/roles
      cd /vagrant/roles
      ansible-galaxy init gearman-server
    SHELL
  end

end
