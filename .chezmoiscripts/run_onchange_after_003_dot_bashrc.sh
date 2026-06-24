#! /bin/bash

bash --login --noprofile --norc -t -c '. ~/.commonrc; export -p' | sed -e 's/declare -x //' | grep -Ee '^ASDF' -e '^GO' -e '^PATH' > $HOME/.config/environment.d/10-path.conf
systemctl --user daemon-reload
