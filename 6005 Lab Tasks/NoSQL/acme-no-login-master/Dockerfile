FROM node:buster-slim

WORKDIR /app

#Install Deps
ADD package.json /app/
RUN npm install

#Install App
ADD index.* /app/

EXPOSE 4242

CMD ["node", "index.js"]