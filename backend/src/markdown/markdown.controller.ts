import * as express from 'express';
const router = express.Router();
router.use(async (req: any, res: any) => {
  try {
    const markdown = req.body.markdown || '';
    const unifiedModule = await import('unified');
    const remarkParse = (await import('remark-parse')).default || (await import('remark-parse'));
    const remarkRehype = (await import('remark-rehype')).default || (await import('remark-rehype'));
    const rehypeSanitize = (await import('rehype-sanitize')).default || (await import('rehype-sanitize'));
    const rehypeStringify = (await import('rehype-stringify')).default || (await import('rehype-stringify'));
    const unified: any = unifiedModule.default || unifiedModule;
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
