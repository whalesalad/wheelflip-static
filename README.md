### Alternator

Like a generator, but better. The state of python/jinja content generators is a mess. The [most popular one](https://github.com/getpelican/pelican) creates a shell script to run a dev server as a background process that writes two pid's to your working directory. What?

My needs are very simple so I am taking it upon myself to create a better one that doesn't have as much cruft.

#### TODO

- Add Markdown rendering capabilities
- Render the sitemap and make it available as jinja context to all pages (particularly for header nav)
- Once the tree of pages/content/metadata is created, traverse this tree and output a static directory structure for deployment
