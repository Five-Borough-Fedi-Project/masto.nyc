# masto.nyc

This is where you can find the Kubernetes yaml that supports masto.nyc. This is going to honestly be a work in progress, and I'll chip away at it when I'm bored. The current to-do list looks like this:

- Provide skeleton files of the ConfigMaps that currently have private info in them
- Once the database is in a state where I want to put it here, add that as well
- Maybe add a pretty diagram for how everything looks, and its dependencies?

Infrastructure To-Dos:
- Use Kustomize to make my life easier
- Set up graylog to play around with the requests floating around
- Grafana looks fun but might be more work than it's worth
- Hook the cronjobs up to the status page