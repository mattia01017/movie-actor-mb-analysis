from src.bitmap import Bitmap

def test_bitmap():
    bitmap = Bitmap(2048)
    
    bitmap.set(1000)
    bitmap.set(2000)
    
    assert bitmap.get(1000)
    assert not bitmap.get(999)
    assert not bitmap.get(1001)
    
    assert bitmap.get(2000)
    assert not bitmap.get(1999)
    assert not bitmap.get(2001)