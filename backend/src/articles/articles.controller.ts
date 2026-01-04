const express = require('express');
const router = express.Router();

// Placeholder service imports (to be implemented)
// const articlesService = require('./articles.service');

// GET /api/articles
router.get('/', async (req, res) => {
  res.json({ message: 'List articles (stub)' });
});

// GET /api/articles/:id
router.get('/:id', async (req, res) => {
  res.json({ message: `Get article ${req.params.id} (stub)` });
});

// POST /api/articles
router.post('/', async (req, res) => {
  // validate auth etc.
  res.status(201).json({ message: 'Create article (stub)' });
});

// PUT /api/articles/:id
router.put('/:id', async (req, res) => {
  res.json({ message: `Update article ${req.params.id} (stub)` });
});

// DELETE /api/articles/:id
router.delete('/:id', async (req, res) => {
  res.status(204).send();
});

module.exports = router;
