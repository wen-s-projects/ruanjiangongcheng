import express from 'express';
import bodyParser from 'body-parser';

const app = express();
app.use(bodyParser.json());

app.get('/health', (req, res) => res.json({ ok: true }));

// Placeholder: Mount modules
app.use('/api/articles', require('./articles/articles.controller'));
app.use('/api/uploads', require('./uploads/uploads.controller'));
app.post('/api/markdown/preview', require('./markdown/markdown.controller'));

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));
