# Box AutoGPT
A Box plug-in for Auto-GPT

### Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository

2. **Install the plugin's dependencies (if any):**
   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   Compress the BoxPlugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ``` shell
   ALLOWLISTED_PLUGINS=BoxPlugin,example-plugin1,example-plugin2,example-plugin3
   ```

   If the plugin is not allowlisted, you will be warned before it's loaded.

6. **Configure .env in AutoGPT:**
   Add your Box App configuration to the bottom of the  `.env` file.

   ``` shell
   ################################################################################
   ### BOX PLUGIN SETTINGS
   ################################################################################
   BOX_DEVELOPER_TOKEN=your_developer_token
   BOX_CLIENT_ID=your_client_id
   BOX_CLIENT_SECRET=your_client_secret
   ```