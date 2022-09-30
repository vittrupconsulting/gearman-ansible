# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ansible.box"

  config.vm.provision "file", source: "roles", destination: "/etc/ansible/roles"
  config.vm.provision "file", source: "ansible_rsa", destination: "/etc/ansible/ansible_rsa"
  config.vm.provision "file", source: "ansible.cfg", destination: "/etc/ansible/ansible.cfg"
  config.vm.provision "file", source: "common.yml", destination: "/etc/ansible/common.yml"

#   config.vm.define "proxy", autostart: false do |proxy|
#     proxy.vm.network "private_network", ip: "192.168.0.152", virtualbox__intnet: true
#     proxy.vm.network "forwarded_port", guest: 22, host: 49152
#     proxy.vm.network "forwarded_port", guest: 80, host: 80
#     proxy.vm.provision "shell", inline: <<-SHELL
#        echo '["gearman-common", "gearman-proxy"]' | tee /etc/ansible/facts.d/roles.fact
#        ansible-playbook --inventory "192.168.0.152," /etc/ansible/common.yml
#     SHELL
#   end

(152..153).each do |i|
  config.vm.define "server-#{i}" do |server|
    server.vm.hostname = "server-#{i}.localhost"
    server.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
    server.vm.network "forwarded_port", guest: "22", host: "49#{i}"
    server.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-server"]' | tee /etc/ansible/facts.d/roles.fact
       ansible-playbook --inventory "192.168.0.#{i}," /etc/ansible/common.yml
    SHELL
  end
end

(154..155).each do |i|
  config.vm.define "worker-#{i}" do |worker|
    worker.vm.hostname = "worker-#{i}.localhost"
    worker.vm.network "private_network", ip: "192.168.0.#{i}", virtualbox__intnet: true
    worker.vm.network "forwarded_port", guest: "22", host: "49#{i}"
    worker.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common", "gearman-worker", "gearman-ansible"]' | tee /etc/ansible/facts.d/roles.fact
       echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
       ansible-playbook --inventory "192.168.0.#{i}," /etc/ansible/common.yml
    SHELL
  end
end

  config.vm.define "client-160" do |client|
    client.vm.box = "gearman.box"
    client.vm.hostname = "client-160.localhost"
    client.vm.network "private_network", ip: "192.168.1.160", virtualbox__intnet: true
    client.vm.network "forwarded_port", guest: "22", host: "49160"
    client.vm.provision "shell", inline: <<-SHELL
       echo '["gearman-common"]' | sudo tee /etc/ansible/facts.d/roles.fact
       echo '["192.168.0.152", "192.168.0.153"]' | tee /etc/ansible/facts.d/servers.fact
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
