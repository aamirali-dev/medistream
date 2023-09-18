# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the React application source code to the container
COPY . .

# Build the React application
RUN npm run build

# Expose the port on which your React app will run (usually 3000)
EXPOSE 3000

# Define the command to start the React app
CMD ["npm", "start"]
