const express = require('express');
const router = express.Router();
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkRehype = require('remark-rehype');
const rehypeStringify = require('rehype-stringify');
const rehypeSanitize = require('rehype-sanitize');

router.use(async (req, res) => {
  try {
    const markdown = req.body.markdown || '';
    const file = await unified()
      .use(remarkParse)
      .use(remarkRehype)
      .use(rehypeSanitize)
      .use(rehypeStringify)
      .process(markdown);
    res.json({ html: String(file) });
  } catch (err) {
    res.status(500).json({ error: 'render error' });
  }
});

module.exports = router;
