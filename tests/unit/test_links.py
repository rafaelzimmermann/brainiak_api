import unittest

from brainiak.utils.links import build_links, get_last_page, get_next_page, get_previous_page, set_query_string_parameter


class LinksTestCase(unittest.TestCase):

    def test_get_previous_page(self):
        self.assertEqual(get_previous_page(1), False)
        self.assertEqual(get_previous_page(5), 4)

    def test_get_next_page(self):
        self.assertEqual(get_next_page(3, 3), False)
        self.assertEqual(get_next_page(9, 20), 10)

    def test_set_query_string_parameter_inexistent(self):
        query_string = "some_key=value_a"
        param_name = "another_key"
        param_value = "value_b"
        computed = set_query_string_parameter(query_string, param_name, param_value)
        expected = "another_key=value_b&some_key=value_a"
        self.assertEqual(computed, expected)

    def test_set_query_string_parameter_existent(self):
        query_string = "same_key=some_value"
        param_name = "same_key"
        param_value = "another_value"
        computed = set_query_string_parameter(query_string, param_name, param_value)
        expected = "same_key=another_value"
        self.assertEqual(computed, expected)

    def test_get_last_page_exact_division(self):
        total_items = 7
        per_page = 7
        computed = get_last_page(total_items, per_page)
        expected = 1
        self.assertEqual(computed, expected)

    def test_get_last_page_exact_division(self):
        total_items = 12
        per_page = 4
        computed = get_last_page(total_items, per_page)
        expected = 3
        self.assertEqual(computed, expected)

    def test_get_last_page_different(self):
        total_items = 11
        per_page = 3
        computed = get_last_page(total_items, per_page)
        expected = 4
        self.assertEqual(computed, expected)

    def test_build_links_without_previous_without_next(self):
        class_uri = "http://class.uri"
        page = 1
        per_page = 1
        request_uri = "http://request.uri"
        total_items = 1
        query_string = ""
        computed = build_links(class_uri, page, per_page, request_uri, total_items, query_string)
        expected = [
            {
                'href': "http://request.uri",
                'rel': "self"
            },
            {
                'href': "http://class.uri",
                'rel': "list"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'rel': "item"
            },
            {
                'href': "http://class.uri",
                'method': "POST",
                'rel': "create"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "DELETE",
                'rel': "delete"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PATCH",
                'rel': "edit"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PUT",
                'rel': "replace"

            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "first"
            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "last"
            }
        ]
        self.assertEqual(computed, expected)

    def test_build_links_without_previous_with_next(self):
        class_uri = "http://class.uri"
        page = 1
        per_page = 1
        request_uri = "http://request.uri"
        total_items = 2
        query_string = ""
        computed = build_links(class_uri, page, per_page, request_uri, total_items, query_string)
        expected = [
            {
                'href': "http://request.uri",
                'rel': "self"
            },
            {
                'href': "http://class.uri",
                'rel': "list"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'rel': "item"
            },
            {
                'href': "http://class.uri",
                'method': "POST",
                'rel': "create"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "DELETE",
                'rel': "delete"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PATCH",
                'rel': "edit"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PUT",
                'rel': "replace"

            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "first"
            },
            {
                'href': "http://class.uri?page=2",
                'method': "GET",
                'rel': "last"
            },
            {
                'href': "http://class.uri?page=2",
                'method': "GET",
                'rel': "next"
            }
        ]
        self.assertEqual(computed, expected)

    def test_build_links_with_previous_without_next(self):
        class_uri = "http://class.uri"
        page = 2
        per_page = 1
        request_uri = "http://request.uri"
        total_items = 2
        query_string = ""
        computed = build_links(class_uri, page, per_page, request_uri, total_items, query_string)
        expected = [
            {
                'href': "http://request.uri",
                'rel': "self"
            },
            {
                'href': "http://class.uri",
                'rel': "list"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'rel': "item"
            },
            {
                'href': "http://class.uri",
                'method': "POST",
                'rel': "create"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "DELETE",
                'rel': "delete"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PATCH",
                'rel': "edit"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PUT",
                'rel': "replace"

            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "first"
            },
            {
                'href': "http://class.uri?page=2",
                'method': "GET",
                'rel': "last"
            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "previous"
            }
        ]
        self.assertEqual(computed, expected)

    def test_build_links_with_previous_with_next(self):
        class_uri = "http://class.uri"
        page = 2
        per_page = 1
        request_uri = "http://request.uri"
        total_items = 3
        query_string = ""
        computed = build_links(class_uri, page, per_page, request_uri, total_items, query_string)
        expected = [
            {
                'href': "http://request.uri",
                'rel': "self"
            },
            {
                'href': "http://class.uri",
                'rel': "list"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'rel': "item"
            },
            {
                'href': "http://class.uri",
                'method': "POST",
                'rel': "create"
            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "DELETE",
                'rel': "delete"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PATCH",
                'rel': "edit"

            },
            {
                'href': "http://class.uri/{resource_id}",
                'method': "PUT",
                'rel': "replace"

            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "first"
            },
            {
                'href': "http://class.uri?page=3",
                'method': "GET",
                'rel': "last"
            },
            {
                'href': "http://class.uri?page=1",
                'method': "GET",
                'rel': "previous"
            },
            {
                'href': "http://class.uri?page=3",
                'method': "GET",
                'rel': "next"
            }
        ]
        self.assertEqual(computed, expected)