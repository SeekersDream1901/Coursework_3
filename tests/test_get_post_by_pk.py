import pytest
from utils import get_post_by_pk

enter_parameters = [
    (1, {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
         'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8f'
                'GVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
         'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было '
                    'так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит,'
                    ' они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. '
                    'Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе.'
                    ' И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы'
                    ' все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
         'views_count': 376, 'likes_count': 154, 'pk': 1}),
    (5, {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
         'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8'
                'fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
         'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я:'
                    ' а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста'
                    ' #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что'
                    ' ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.',
         'views_count': 287, 'likes_count': 99, 'pk': 5}),
    (8, {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
         'pic': 'https://images.unsplash.com/photo-1494952200529-3ceb822a75e2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8'
                'fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
         'content': 'Утром отправились на катере обследовать ближайшие острова – острова в основном каменные, беспо'
                    'лезные и необитаемые. На обратном пути попали в бурю, и нас чуть не унесло в океан. В течение '
                    '10 минут наш катер несся к отмели, а потом мы стали дрейфовать между скал, держась за трос. '
                    'Наконец погода наладилась и мы смогли совершить обратный путь. Когда уже прибыли домой, я '
                    'попросил, чтобы на следующий день нам устроили на катере экскурсию по морю. Нас провели по '
                    'морскому дну от одного острова к другому, показали различные интересные объекты, которые '
                    'встречаются в этом районе.',
         'views_count': 141, 'likes_count': 45, 'pk': 8}),
    (9, None)
]


@pytest.mark.parametrize("pk, output", enter_parameters)
def test_get_post_by_pk(pk, output):
    assert get_post_by_pk(pk) == output, f"Ошибка для {pk}"