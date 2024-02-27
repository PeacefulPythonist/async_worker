# Async Worker

Async Link Worker is a Python library for asynchronously processing a list of links using custom asynchronous functions. It provides functionality to execute asynchronous operations on links, retrying in case of errors, and handling the results efficiently.

## Usage

Here's a simple example demonstrating how to use Async Link Worker:

```python
import random
import asyncio
from async_worker import process_links


async def fetch_data(link):
    range_index = link[1]
    link = link
    # Asynchronous function to fetch data from a URL
    # This function can be customized as per requirement
    # For demonstration purposes, we'll just print the URL
    print(f"Fetching data from: {url}")
    await asyncio.sleep(random.random())  # Simulating async operation
    return url, "Data"  # Returning a tuple containing URL and fetched data

async def main():
    links = ["https://example.com", "https://example.org"]
    results = await process_links(links, fetch_data)
    print(results)

asyncio.run(main())
```
If you want to use the library within a synchronous function, you can use the - `sprocess_links` function directly within your synchronous code. Here's an example:

```python
from async_worker import sprocess_links
#Your code...
def main_sync():
    links = ["https://example.com", "https://example.org"]
    results = sprocess_links(links, fetch_data)
    print(results)

main_sync()
```

## API Reference

### `process_links(links, async_func, try_count=5, return_results=True, ignor_error=False)`

Apply async_func to all links, retrying for a certain number of times if errors occur.

- `links` (List): List of links to apply async_func to.
- `async_func` (Callable): Asynchronous function to apply to each link.
- `try_count` (int): Number of retry attempts in case of errors. Default is 5.
- `return_results` (bool): Flag indicating whether to return results. Default is True.
- `ignor_error` (bool): Flag indicating whether to ignore errors. Default is False.

Returns:
- List: List of results obtained from applying async_func to links.


### `sprocess_links(links, async_func, try_count=5, return_results=True, ignor_error=False)`

Synchronous wrapper for `process_links`.

### `filtering_tuple(results, to_tuple=True)`

Filter results based on whether they are tuples or not.

- `results` (List): List of results to filter.
- `to_tuple` (bool): Flag indicating whether to filter tuples or non-tuples. Default is True.

Returns:
- List: Filtered list of results.

### `result_links(links, async_func)`

Apply async_func to all links concurrently.

- `links` (List[Tuple]): List of links to apply async_func to.
- `async_func` (Callable): Asynchronous function to apply to each link.

Returns:
- List: List of results obtained from applying async_func to links.
