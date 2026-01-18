
import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/healthz', (_req, res) => res.status(200).send('ok'));

app.get('/', (req, res) => {
  res.json({
    service: 'node-app',
    message: 'Hello from Node.js!',
    path_hint: 'Access via /node/',
    headers: req.headers
  });
});

app.listen(PORT, () => {
  console.log(`Node app listening on port ${PORT}`);
});
