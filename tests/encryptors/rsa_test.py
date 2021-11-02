import pytest

from encryptor.encryptors import Rsa
from encryptor.errors import *


def test_encrypt():
    assert (
        Rsa.encrypt("CRYPTO IS FUN", None, None)
        == "5973239413136de296b6008c9c8f377935888db181291fe0aedfa90e6dd55c87"
    )
    assert (
        Rsa.encrypt("CRYPTO IS FUN", None, 3)
        == "e9fc08dd8e5979767c64e2907f06d148a9d21a53ba41d96e24c211cac893ea1"
    )
    assert (
        Rsa.encrypt(
            "THIS IS A SECRET MESSAGE",
            5787569202628183729950832880652727754005719771773093134642433446165156045800940260069420455872284754818611398500172181804200252032228416613272163386513407,
            None,
        )
        == "fda861718f15d3f93a34e16234cb9e2e1253609f5386e4a2d039cf264f24629b8a056d79bb9d99188c4b38f019755f2efb649f6bd7018746208b540457eaec7"
    )
    assert (
        Rsa.encrypt(
            "THIS IS ANOTHER SECRET MESSAGE",
            1333587085548542000125728320363569995153784703484871546886767172788839430007526423879518222597487552970882011628414157261,
            17,
        )
        == "4d8d01106319c92acd351d4ea6a901262d9aae1587e7097ef296beac66d2f057e5e2a289b66460e08778432f614171781d42"
    )


def test_decrypt():
    assert (
        Rsa.decrypt(
            "12e147bec39ea02f983d27456302bb02bb3513d987d10f63493b996cf833643e",
            None,
            None,
            None,
        )
        == "68656c6c6f"
    )
    assert (
        Rsa.decrypt(
            "13b401f6c90f2f67767f96ebc1b1a11f8d0def5a9e0d95ef228f1a96a98fe933cfaa2658936cbad2ad21544e42edc85924f1",
            1000702551822989690372604004700059282806706303160420382744019,
            1076488452489092570355294835057204962265820348661574294844261,
            None,
        )
        == "63727970746f2069732066756e"
    )
    assert (
        Rsa.decrypt(
            "48fc2ca96c4d19c6346afec5c2a153a0514534ff8df083630fa8a4853de1decc0b6e997255f9a6a5d267ee072b992f6bb8e7",
            1495642814741103912463343960249087350092163171914191197701823,
            1071378214470101651807067578682885425616229449736925993550017,
            17,
        )
        == "74686973206973206120736563726574206d657373616765"
    )
