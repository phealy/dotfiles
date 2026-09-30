# User-Wide Copilot Instructions

## General instructions

- Whenever you do something involving dates, run the date command in the shell and use that as the current date and time.
- Whenever you're comparing dates, use a shell script or Python script to do it.
- Whenever you're comparing versions, use `dpkg --compare-versions` if available.
- Don't add nolint or delete tests to resolve issues unless specifically requested; check with the user first.
- When you're working in a repo, prefer to work in a separate worktree in a temporary directory you own to avoid issues with other changes.
- If you need to push container images for local-based testing, use pahealyaks.azurecr.io
- If you need to log into to pahealyaks.azurecr.io, use the command 'az acr login --subscription c1089427-83d3-4286-9f35-5af546a6eb67 -g pahealy-devbox -n pahealyaks'
- I have workloads in both microsoft.com and the TME tenant; make sure you're in the correct one when getting a token.
- If you're attempting to use azure bastion to SSH to a node via az bastion ssh, always pass the --subscription argument with the subscription ID. Otherwise, if the current default subscription is in the wrong tenant, you will see a timeout issue.
- When using Azure CLI, always use --subscription and --resource-group instead of relying on the defaults not to change.
- When using kubectl, always use --context and --namespace instead of relying on the defaults not to change.
- When you create resources in Azure for testing, tag them with copilot-session '<yoursessionId>' to make cleanup easier
- When trying to use Azure Bastion SSH, it will fail with a connection time out if the active Azure subscription is from a different tenant than the Bastion resource.
- If a request involved doing something instead of just answering a question, send a push notification via the Pushover API to notify the user that work has finished. `~/.local/bin/pushover "<TITLE>" "<SUMMARY>"` (the title must be <=250 characters and the message must be <=1024 characters)
- If you need to refresh the TME login, the command is 'az login --tenant 70a036f6-8e4d-4615-bad6-149c02e7720d </dev/null'
