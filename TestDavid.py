import unittest
from unittest.mock import Mock
from twitter_ap import AppTwitter
from Tweet import *
from baseladvd import basedb

class Test(unittest.TestCase):

    def setUp(self):
        
        self.tw = AppTwitter()
        self.usuariomock = Mock(user_id = "2903096308", handle = "MugetsuZero", lugar = "Saltillo Coahuila",\
        verificado = "Usuario no verificado.",  followers = 3, numtweets = 14, friends = 75,\
        description = "No tiene.", lenguaje = "es",\
         profile = "http://pbs.twimg.com/profile_images/539929455871811584/rm23envR_normal.jpeg",\
         Ranking = None,Categoria = None,Victorias = 0,Derrotas = 0)
        self.usuario = Tweeti(self.usuariomock.user_id,self.usuariomock.handle,self.usuariomock.lugar,\
        self.usuariomock.verificado,self.usuariomock.followers,self.usuariomock.numtweets,\
        self.usuariomock.friends,self.usuariomock.description,self.usuariomock.lenguaje,\
        self.usuariomock.profile,self.usuariomock.Ranking,self.usuariomock.Categoria,self.usuariomock.Victorias,\
        self.usuariomock.Derrotas)

        self.sql = basedb()
        self.sql.insert_db(self.usuario)

        self.usuario1 = Tweeti('12345','Velocito','Lolazo','chi',500,100,700,'velocito !','es','url',None,None,0,0)

    def tearDown(self):
        print("Fin de la prueba")

    #Hace las pruebas de guardar
    def test_Usuario(self):

        print("test_Usuario")
        self.assertEqual(self.usuario1.user_id, '12345')
        self.assertEqual(self.usuario1.handle, 'Velocito')
        self.assertEqual(self.usuario1.lugar, 'Lolazo' )
        self.assertEqual(self.usuario1.verificado, "chi" )
        self.assertEqual(self.usuario1.followers, 500 )
        self.assertEqual(self.usuario1.numtweets, 100 )
        self.assertEqual(self.usuario1.friends, 700 )
        self.assertEqual(self.usuario1.description, 'velocito !')
        self.assertEqual(self.usuario1.lenguaje, 'es')
        self.assertEqual(self.usuario1.profile, 'url')
        self.assertEqual(self.usuario1.Ranking, None)
        self.assertEqual(self.usuario1.Categoria, None)
        self.assertEqual(self.usuario1.Victorias, 0)
        self.assertEqual(self.usuario1.Derrotas, 0)

        #Tipo de dato
        self.assertNotEqual(self.usuario1.followers, '500' )
        self.assertNotEqual(self.usuario1.numtweets, '100' )
        self.assertNotEqual(self.usuario1.friends, '700')
        self.assertNotEqual(self.usuario1.Victorias, '0')
        self.assertNotEqual(self.usuario1.Derrotas, '0')


    def testinsert(self):
        print("testinsert")
        self.assertTrue(self.sql.insert_db(self.tw.getUsuario("MugetsuZero")))

    def testupdate(self):
        print("test_update")
        self.assertTrue(self.sql.updateUsuario(self.usuario.handle,self.usuario.Ranking,\
        self.usuario.Categoria,self.usuario.Victorias,self.usuario.Derrotas))

    def testborrar(self):
        print("test_borrar")
        self.assertTrue(self.sql.deleteUsuario(self.usuario.handle))

    def test_getUsuario(self):
        print("test_getUsuario")
        self.assertEqual(self.tw.getUsuario("MugetsuZero").user_id, self.usuario.user_id)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").handle, self.usuario.handle)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").lugar, self.usuario.lugar)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").verificado, self.usuario.verificado)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").followers, self.usuario.followers)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").numtweets, self.usuario.numtweets)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").friends, self.usuario.friends)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").description, self.usuario.description)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").lenguaje, self.usuario.lenguaje)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").profile, self.usuario.profile)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").Ranking, self.usuario.Ranking)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").Categoria, self.usuario.Categoria)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").Victorias, self.usuario.Victorias)
        self.assertEqual(self.tw.getUsuario("MugetsuZero").Derrotas, self.usuario.Derrotas)

if __name__ == '__main__':
    unittest.main()
