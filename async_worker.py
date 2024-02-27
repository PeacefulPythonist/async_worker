import asyncio
from typing import List, Callable, Any, Tuple

async def filtering_tuple(results: List[Any], to_tuple: bool = True) -> List:
    """
    Filter results based on whether they are tuples or not.

    Args:
    - results (List): List of results to filter.
    - to_tuple (bool): Flag indicating whether to filter tuples or non-tuples.

    Returns:
    - List: Filtered list of results.
    """
    if to_tuple:
        key_func = lambda result: isinstance(result, tuple)
    else:
        key_func = lambda result: not isinstance(result, tuple)

    return list(filter(key_func, results))


async def result_links(links: List[Tuple], async_func: Callable) -> List:
    """
    Apply async_func to all links concurrently.

    Args:
    - links (List[Tuple]): List of links to apply async_func to.
    - async_func (Callable): Asynchronous function to apply.

    Returns:
    - List: List of results obtained from applying async_func to links.
    """
    tasks = [async_func(link) for link in links]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results


async def process_links(links: List, async_func: Callable, try_count: int = 5, return_results: bool = True, ignor_error: bool = False) -> List:
    """
    Apply async_func to all links, retrying for a certain number of times if errors occur.

    Args:
    - links (List): List of links to apply async_func to.
    - async_func (Callable): Asynchronous function to apply.
    - try_count (int): Number of retry attempts in case of errors.
    - return_results (bool): Flag indicating whether to return results.
    - ignor_error (bool): Flag indicating whether to ignore errors.

    Returns:
    - List: List of results obtained from applying async_func to links.
    """
    if not (isinstance(links, list) or isinstance(links, tuple)):
        links, async_func = async_func, links

    links = [(link, i) for i, link in enumerate(links)]
    all_results = []

    for i in range(try_count):
        results = await result_links(links, async_func)

        error_links = [
            links[j] 
            for j, result in enumerate(results)
            if not isinstance(result, tuple)
        ]

        if not error_links:
            break

        links = error_links

    if (try_count - 1 == i) and not ignor_error:
        raise Exception("\nAn error occurred during asynchronous execution\n")


    if return_results:
        all_results = await filtering_tuple(all_results)
        all_results = sorted(all_results, key=lambda result: result[0])
        return all_results


def sync_process_links(links: List, async_func: Callable, try_count: int = 5, return_results: bool = True, ignor_error: bool = False) -> List:
    """Synchronous wrapper for process_links."""
    return asyncio.run(process_links(links, async_func, try_count, return_results, ignor_error))
