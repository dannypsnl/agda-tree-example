# Literate agda for forester

The repository use `forester` v4.3.1, produced by command `forester init`

## Steps

In `quark/` run

```
agda --html --html-highlight=code bool.lagda.tree
agda-tree build
```

Back to root of the repository

* modify `forest.toml`, add `quark/trees` to `trees`
* modify `forest.toml`, add `quark/html` to `assets`
* modify `theme/tree.xsl`

## Modify to `tree.xsl`

```diff
       <head>
         <meta name="viewport" content="width=device-width" />
         <link rel="stylesheet" href="style.css" />
+        <link rel="stylesheet" href="Agda.css" />
         <link rel="stylesheet" href="katex.min.css" />
         <script type="text/javascript">
           <xsl:if test="/f:tree/f:frontmatter/f:source-path">
```
