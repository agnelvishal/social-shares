# Social shares

[![Build Status](https://travis-ci.org/debrouwere/social-shares.svg?branch=master)](https://travis-ci.org/debrouwere/social-shares)

A command-line utility and Python library to access the social share counts for a particular URL.

**Note:** unfortunately this utility can no longer be used to fetch tweet and retweet counts,
as Twitter has removed the API this functionality relied on. Facebook and other platforms
still work.

### Usage

```
Usage:
  socialshares <url> [<platforms>...] [options]

Options:
  -h, --help  Show this screen.
  -p, --plain  Plain output.
  -r <attempts>, --retry <attempts>  Retry fetching up to <attempt> times [default: 1]
  -e, --exit  Exit with an error code when not all counts could be fetched.
```

Some examples:

```sh
# fetch count for all supported platforms,
# try again once (the default) for platforms that fail
$ socialshares http://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/

# fetch only facebook
$ socialshares http://www.theguardian.com/politics facebook     --retry 2
```

### Supported platforms

Platform    | Description
----------- | -----------
facebook    | facebook shares and comments
pinterest   | pinterest pins
reddit      | reddit ups and downs (summed across posts)

Platforms are fetched in parallel and retried (once by default.)
If no platforms are specified, just facebook and twitter will be returned.

### Unsupported platforms

The following APIs unfortunately no longer exist, and have been removed from the interface.

Platform    | Description
----------- | -----------
twitter     | twitter tweets and retweets containing the URL
linkedin    | linkedin shares
google      | google +1's

### Output

By default, `socialshares` outputs JSON:

```json
{
  "reddit": {
    "downs": 0,
    "ups": 6
  },
  "facebook": 1498,
  "pinterest": 1
}
```

Use the `--plain` flag if instead you'd like space-separated output.

```sh
$ socialshares http://www.theguardian.com/politics twitter
57
```

### Usage from Python

```python
import socialshares
counts = socialshares.fetch(url, ['facebook', 'pinterest'])
```

### Installation

```sh
pip install socialshares
# optionally, for asynchronous fetching
pip install grequests
```

If [requests_futures][requests_futures] and (for Python 2.x) [futures][futures]
are installed, `social-shares` will use these packages to speed up share count
fetching, by accessing the various social media APIs in parallel.

[requests_futures]: https://github.com/ross/requests-futures
[futures]: https://code.google.com/p/pythonfutures/
