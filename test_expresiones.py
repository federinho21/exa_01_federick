import contextlib
import io
import runpy
import unittest
from unittest.mock import patch

from Subrutinas import validar_expresion


class PruebasExpresiones(unittest.TestCase):
    def test_ejemplos_y_errores(self):
        casos = [
            ("a+(b*c)", True, ""),
            ("a+(b*c", False, "falta cerrar"),
            ("a+b*c)", False, "sin apertura"),
            ("a+(b*c]", False, "se esperaba ')'"),
            ("fx = a + { 4.5 * [ ( b/c ) - ( c*c ) ] }", True, ""),
            ("([)]", False, "se esperaba ']'"),
            ("a+b", True, ""),
        ]
        for expresion, esperado, detalle in casos:
            with self.subTest(expresion=expresion):
                valido, error = validar_expresion(expresion)
                self.assertEqual(valido, esperado)
                self.assertIn(detalle, error)
                if valido:
                    self.assertEqual(error, "")

    def test_menu_repite_y_rechaza_opcion(self):
        salida = io.StringIO()
        with patch('builtins.input', side_effect=['9', '1', '(]', '1', '()', '3']), contextlib.redirect_stdout(salida):
            runpy.run_path('main.py')
        self.assertIn('opcion incorrecta', salida.getvalue())
        self.assertIn("se esperaba ')'", salida.getvalue())
        self.assertIn('esta bien escrita', salida.getvalue())


if __name__ == '__main__':
    unittest.main()
