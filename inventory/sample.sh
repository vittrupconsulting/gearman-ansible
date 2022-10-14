#!/bin/sh

cat << EOF
{
  "Enrolled": {
    "hosts": [
      "ansible157",
      "ansible158"
    ]
  },
  "Enrolled2": {
    "hosts": [
      "ansible157",
      "ansible158"
    ]
  },
  "_meta": {
    "hostvars": {
      "ansible157": {
        "global_server_domain": "mydomain.local"
      },
      "ansible158": {
        "global_server_domain": "mydomain.local"
      }
    }
  }
}
EOF