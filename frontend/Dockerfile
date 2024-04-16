from node:20

WORKDIR /app

RUN chown -R node:node /app

USER node

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
