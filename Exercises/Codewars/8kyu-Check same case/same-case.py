def same_case(a, b): 
    # your code here
    pass

import codewars_test as test

@test.describe("Basic Tests")
def test_group():
    @test.it("basic test case")
    def test_case():
        test.assert_equals(same_case('C', 'B'), 1)
        test.assert_equals(same_case('b', 'a'), 1)
        test.assert_equals(same_case('d', 'd'), 1)
        test.assert_equals(same_case('A', 's'), 0)
        test.assert_equals(same_case('c', 'B'), 0)
        test.assert_equals(same_case('b', 'Z'), 0)
        test.assert_equals(same_case('\t', 'Z'), -1)
        test.assert_equals(same_case('H', ':'), -1)
