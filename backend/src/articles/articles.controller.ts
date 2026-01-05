import * as express from 'express';
const router = express.Router();

// Placeholder service imports (to be implemented)
// const articlesService = require('./articles.service');

// GET /api/articles
router.get('/', async (req: any, res: any) => {
  res.json({ message: 'List articles (stub)' });
});

// GET /api/articles/:id
router.get('/:id', async (req: any, res: any) => {
  res.json({ message: `Get article ${req.params.id} (stub)` });
});

// POST /api/articles
router.post('/', async (req: any, res: any) => {
  // validate auth etc.
  res.status(201).json({ message: 'Create article (stub)' });
});

// PUT /api/articles/:id
router.put('/:id', async (req: any, res: any) => {
  res.json({ message: `Update article ${req.params.id} (stub)` });
});

// DELETE /api/articles/:id
router.delete('/:id', async (req: any, res: any) => {
  res.status(204).send();
});

module.exports = router;
