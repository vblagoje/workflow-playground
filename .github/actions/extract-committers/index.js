const { execSync } = require('child_process');
const core = require('@actions/core');

try {
  // Get inputs from the action
  const projectDir = core.getInput('project_dir');
  const namesHandlesJson = core.getInput('names_handles');

  // Parse the names to handles mapping from JSON input
  const namesHandles = JSON.parse(namesHandlesJson);

  // Extract committers' names from the git log
  const result = execSync(`git log --pretty="%an" -- ${projectDir}`).toString();
  const committers = new Set(result.trim().split('\n'));

  // Filter committers based on predefined list
  const filteredHandles = [];
  committers.forEach(name => {
    if (namesHandles[name]) {
      filteredHandles.push(namesHandles[name]);
    }
  });

  // Pick a random handle from the list
  const randomUser = filteredHandles.length > 0 ? filteredHandles[Math.floor(Math.random() * filteredHandles.length)] : null;

  // Output the randomly selected user
  core.setOutput('user', randomUser);
} catch (error) {
  core.setFailed(`Action failed with error: ${error.message}`);
}
