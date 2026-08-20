# User-Wide Copilot Instructions

## General instructions

- Whenever you do something involving dates, run the date command in the shell and use that as the current date and time.
- Whenever you're comparing dates, use a shell script or Python script to do it.
- Whenever you're comparing versions, use `dpkg --compare-versions` if available.
- Don't add nolint or delete tests to resolve issues unless specifically requested; check with the user first.

## Azure interactions

- If you need to push container images for local-based testing, use pahealyaks.azurecr.io
- If you need to log into to that container registry, use the command 'az acr login --subscription c1089427-83d3-4286-9f35-5af546a6eb67 -g pahealy-devbox -n pahealyaks'
- I have workloads in both microsoft.com and the TME tenant; make sure you're in the correct one when getting a token.
- If you need to refresh the TME login, the command is 'az login --tenant 70a036f6-8e4d-4615-bad6-149c02e7720d </dev/null'
- When trying to use Azure Bastion SSH, it will fail with a connection time out if the active Azure subscription is from a different tenant than the Bastion resource.

## Task Completion Notifications

If a request involved doing something instead of just answering a question, send a push notification
via the Pushover API to notify the user that work has finished.

Use the following bash command to send the notification:

```bash
curl -s -F "token=$PUSHOVER_API_KEY" -F "user=$PUSHOVER_USER_KEY" -F "title=GitHub Copilot request complete" -F "message=<SUMMARY>" https://api.pushover.net/1/messages.json
```

Requirements:
- Source `~/.pushover` to load the environment variables before sending.
- The Pushover API token is stored in the environment variable `PUSHOVER_API_KEY`.
- The Pushover user key is stored in the environment variable `PUSHOVER_USER_KEY`.
- Replace `<SUMMARY>` with a brief plain-text summary of the work that was completed.
- The title must be <=250 characters and the message must be <=1024 characters.
- Do not log or display the API key or user key values.
- If the environment variables are not set, skip the notification silently.

