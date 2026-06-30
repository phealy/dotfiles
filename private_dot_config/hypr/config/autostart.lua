-- Auto-start config
-- if you dont use UWSM add your auto start programs here, otherwise use XDG autostart https://wiki.archlinux.org/title/XDG_Autostart

hl.on("hyprland.start", function ()
    hl.exec_cmd("dbus-update-activation-environment --systemd --all")
    hl.exec_cmd("qs -c noctalia-shell")
    hl.exec_cmd("xhost +SI:localuser:root")
    hl.exec_cmd("gnome-keyring-unlock.sh")
    hl.exec_cmd("keepassxc-secretstore")
    hl.exec_cmd("/opt/microsoft/msedge/microsoft-edge")
    hl.exec_cmd("/opt/microsoft/msedge/microsoft-edge --profile-directory=Default --app-id=eoficlgicibekocmfdomjbfnjmehnhcd --app-url=https://outlook.cloud.microsoft/mail/ %U")
    hl.exec_cmd("/opt/microsoft/msedge/microsoft-edge --profile-directory=Default --app-id=ompifgpmddkgmclendfeacglnodjjndh --app-url=https://teams.cloud.microsoft/?clientType=pwa %U")
end)
