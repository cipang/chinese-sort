# chinese-sort
A Python 3 library to sort Traditional Chinese strings by the number of strokes and frequency. This code uses Unicode and Unihan data.

# Usage
1. Download both sortdata.py and sortfunc.py to your project.
2. `import sortfunc`
3. Use Python sort functions (e.g. `sorted`) and supply `sortfunc.chinese_sort_key` as the `key` function.

## Example
<pre><code>import sortfunc
sorted([...], key=sortfunc.chinese_sort_key)</code></pre>

# Update Database
This project uses the data of Unihan. Whenever a new version of Unihan releases, run `gen_dict.py` to create an update `sortdata` module as follows:

1. Download the data from http://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip
2. Unzip the archive.
3. Run `python3 gen_dict.py (path)`, where `path` is the path to the extracted `Unihan_DictionaryLikeData.txt`.

