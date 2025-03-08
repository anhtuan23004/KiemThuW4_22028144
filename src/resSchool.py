import unittest

def get_result(diem_chuan, diem_chuyen):
    if diem_chuan >= 42 and diem_chuyen >= 8.5:
        return "chuyen 1"
    elif diem_chuan >= 41 and diem_chuyen >= 8:
        return "chuyen 2"
    else:
        return "chuc ban may man lan sau"


def main():
    diem_chuan = float(input("Enter standard score (diem chuan): "))
    diem_chuyen = float(input("Enter special score (diem chuyen): "))
    result = get_result(diem_chuan, diem_chuyen)
    print(result)


if __name__ == "__main__":
    main()


class TestSchoolResult(unittest.TestCase):
    def test_chuyen1(self):
        self.assertEqual(get_result(43, 9), "chuyen 1")
    
    def test_chuyen2(self):
        self.assertEqual(get_result(41.5, 8), "chuyen 2")
    
    def test_fail(self):
        self.assertEqual(get_result(30, 5), "chuc ban may man lan sau")


if __name__ == "__main__":
    unittest.main()