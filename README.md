# Literate agda for forester

Instructions for `forester` v5.0, initial repository produced by command `forester init`.

## Steps

In `quark/` run

```
agda --html --html-highlight=code bool.lagda.tree
agda-tree build
```

Back to root of the repository

- modify `forest.toml`, add `quark/trees` to `trees`
- modify `forest.toml`, add `quark/html` to `assets`
- modify `theme/tree.xsl` (see below)
- run `forester build`
- open `quark/bool.xml` in your browser

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
