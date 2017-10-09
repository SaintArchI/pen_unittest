from Pen import Pen
import pytest

import io
from contextlib import redirect_stdout

class TestPenConstructor:
    @pytest.fixture() #before method
    def createPen(self):
        testPen = Pen()
        return testPen

    def test_constrDefault(self, createPen):
        assert createPen is not None

    @pytest.mark.parametrize('inkVal', [0, 10, 100])
    @pytest.mark.parametrize('letSize', [0, 2, 10, 100])
    @pytest.mark.parametrize('clr', ['red', 'black', 'pink'])
    def test_constrWithParamPositive(self, createPen, inkVal, letSize, clr):
        createPen.ink_container_value = inkVal
        createPen.size_letter = letSize
        createPen.color = clr
        assert createPen is not None

    @pytest.mark.parametrize('inkVal', [-1, -10])
    @pytest.mark.parametrize('letSize', [-1, -5])
    @pytest.mark.xfail
    def test_constrWithParamNegative(self, createPen, inkVal, letSize):
        createPen.ink_container_value = inkVal
        createPen.size_letter = letSize
        assert createPen is None


class TestPenWriting():
    @pytest.fixture() #before method
    def createPen(self):
        testPen = Pen()
        return testPen

    @pytest.mark.parametrize('word', ['a', 'word', 'constructor', 'this is the text'])
    @pytest.mark.parametrize('letSize', [1.0, 2.0, 5.0])
    def test_write_differentWordLengthAndSize(self, createPen, word, letSize):
        createPen.size_letter = letSize
        assert createPen.write(word) == word

    @pytest.mark.parametrize('word', ['a'])
    @pytest.mark.parametrize('inkVal', [0])
    def test_write_noInk(self, createPen, word, inkVal):
        createPen.ink_container_value = inkVal
        assert createPen.write(word) == ''

    @pytest.mark.parametrize('word', ['longword', 'another word'])
    @pytest.mark.parametrize('inkVal', [10])
    @pytest.mark.parametrize('letSize', [1.0, 2.0, 2.5, 5.0])
    def test_write_partOfWord(self, createPen, word, inkVal, letSize):
        createPen.ink_container_value = inkVal
        assert createPen.write(word) == word[0:inkVal//int(letSize)]



class TestPenState():
    @pytest.fixture()  # before method
    def createPen(self):
        testPen = Pen()
        return testPen

    @pytest.mark.parametrize('inkValue', [1000, 500, 10])
    def test_check_pen_statePositive(self, createPen, inkValue):
        createPen.ink_container_value = inkValue
        assert createPen.check_pen_state() is True

    @pytest.mark.parametrize('inkValue', [0, -10, -100])
    def test_check_pen_stateNegative(self, createPen, inkValue):
        createPen.ink_container_value = inkValue
        assert createPen.check_pen_state() is False

class TestPenOtherOptions():
    @pytest.mark.parametrize('clr', ['red', 'pink', 'black'])
    def test_get_color(self, clr):
        assert Pen(color=clr).get_color() == clr

    def test_do_something_else(self):
        testPen = Pen()
        stdOut = io.StringIO()
        with redirect_stdout(stdOut):
            testPen.do_something_else()
        assert stdOut.getvalue().rstrip() == testPen.color