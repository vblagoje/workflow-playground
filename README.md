# workflow-playground
This is a playground for testing GitHub Actions and Workflows.
Rather than playing with the actual repository, I'm going to use this repository to test out different workflows and actions.

## Workflows
One can see all the workflows in the `.github/workflows` directory.
Currently, there is only one workflow:
- `test-update-pr.yml` - This workflow is triggered when a pull request is opened or updated. It runs a script to update the pull request description with a list of files that have been modified.
