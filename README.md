# Literate agda for forester

Instructions for `forester` v5.0, initial repository produced by command `forester init`.

## Steps

In the root of the repository

```
agda --html --html-highlight=code lagda/bool.lagda.tree
```

- modify `forest.toml`, add `html` to `trees`
- modify `theme/tree.xsl` (see below)
- run `forester build`
- `cp html/Agda.css output/`
- run `uv run copy-index.py`
- open `output/bool/index.xml` in your browser

## Modification to `tree.xsl`

Link the Agda style as follows:

```diff
       <head>
         <meta name="viewport" content="width=device-width" />
         <link rel="stylesheet" href="{/f:tree/@base-url}style.css" />
+        <link rel="stylesheet" href="{/f:tree/@base-url}Agda.css" />
         <link rel="stylesheet" href="{/f:tree/@base-url}katex.min.css" />
         <script type="text/javascript">
           <xsl:if test="/f:tree/f:frontmatter/f:source-path">
```
