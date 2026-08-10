import setting
from playersdata import pdata
from stats import mystats

import babase
import bascenev1 as bs

sett = setting.get_settings_data()


# Per-role tag animations. Add a "taganim" array to any role in roles.json
# with a list of (time, (r,g,b)) tuples, e.g.:
#   "taganim": [[0.0, [1,0.6,0]], [1.0, [1,1,0]], [2.0, [1,0.6,0]]]
# If not set, the default rainbow animation is used.
ROLE_ANIMS = {
    "owner": {0.0: (1.5, 0, 0), 0.15: (0.05, 0, 0), 0.3: (1.5, 0.1, 0.1),
              0.45: (0.05, 0, 0), 0.6: (1.5, 0, 0), 0.75: (0.4, 0, 0),
              0.9: (1.5, 0.05, 0.05), 1.05: (0.05, 0, 0), 1.2: (1.5, 0, 0)},
}

DEFAULT_ANIM = {0.2: (2, 0, 2), 0.4: (2, 2, 0), 0.6: (0, 2, 2),
                0.8: (2, 0, 2), 1.0: (1, 1, 0), 1.2: (0, 1, 1),
                1.4: (1, 0, 1)}


def addtag(node, player):
    session_player = player.sessionplayer
    account_id = session_player.get_v1_account_id()
    customtag_ = pdata.get_custom()
    customtag = customtag_['customtag']
    roles = pdata.get_roles()
    p_roles = pdata.get_player_roles(account_id)
    tag = None
    col = (0.5, 0.5, 1)
    role_name = None
    if account_id in customtag:
        tag = customtag[account_id]
    elif p_roles != []:
        for role in roles:
            if role in p_roles:
                role_name = role
                tag = roles[role]['tag']
                col = (
                    0.7, 0.7, 0.7) if 'tagcolor' not in roles[role] else \
                    roles[role]['tagcolor']
                break
    if tag:
        Tag(node, tag, col, role_name=role_name)


def addrank(node, player):
    session_player = player.sessionplayer
    account_id = session_player.get_v1_account_id()
    rank = mystats.getRank(account_id)

    if rank:
        Rank(node, rank)


def addhp(node, spaz):
    def showHP():
        hp = spaz.hitpoints
        if spaz.node.exists():
            HitPoint(owner=node, prefix=str(int(hp)),
                     position=(0, 1.75, 0), shad=1.4)
        else:
            spaz.hptimer = None
    spaz.hptimer = bs.Timer(2, babase.CallStrict(
        showHP), repeat=True)


class Tag(object):
    def __init__(self, owner=None, tag="somthing", col=(1, 1, 1),
                 role_name=None):
        self.node = owner

        mnode = bs.newnode('math',
                           owner=self.node,
                           attrs={
                               'input1': (0, 1.5, 0),
                               'operation': 'add'
                           })
        self.node.connectattr('torso_position', mnode, 'input2')
        if '\\' in tag:
            tag = tag.replace('\\d', ('\ue048'))
            tag = tag.replace('\\c', ('\ue043'))
            tag = tag.replace('\\h', ('\ue049'))
            tag = tag.replace('\\s', ('\ue046'))
            tag = tag.replace('\\n', ('\ue04b'))
            tag = tag.replace('\\f', ('\ue04f'))
            tag = tag.replace('\\g', ('\ue027'))
            tag = tag.replace('\\i', ('\ue03a'))
            tag = tag.replace('\\m', ('\ue04d'))
            tag = tag.replace('\\t', ('\ue01f'))
            tag = tag.replace('\\bs', ('\ue01e'))
            tag = tag.replace('\\j', ('\ue010'))
            tag = tag.replace('\\e', ('\ue045'))
            tag = tag.replace('\\l', ('\ue047'))
            tag = tag.replace('\\a', ('\ue020'))
            tag = tag.replace('\\b', ('\ue00c'))

        self.tag_text = bs.newnode('text',
                                   owner=self.node,
                                   attrs={
                                       'text': tag,
                                       'in_world': True,
                                       'shadow': 1.0,
                                       'flatness': 1.0,
                                       'color': tuple(col),
                                       'scale': 0.01,
                                       'h_align': 'center'
                                   })
        mnode.connectattr('output', self.tag_text, 'position')

        # Pick animation: role-specific > role's custom "taganim" > default
        anim_keys = None
        if sett["enableTagAnimation"]:
            if role_name and role_name in ROLE_ANIMS:
                anim_keys = ROLE_ANIMS[role_name]
            elif role_name:
                roles = pdata.get_roles()
                if role_name in roles and "taganim" in roles[role_name]:
                    anim_keys = {
                        float(k): tuple(v) for k, v in
                        roles[role_name]["taganim"]
                    }
            if anim_keys is None:
                anim_keys = DEFAULT_ANIM

        if anim_keys:
            bs.animate_array(node=self.tag_text, attr='color', size=3,
                             keys=anim_keys, loop=True)


class Rank(object):
    def __init__(self, owner=None, rank=99):
        self.node = owner
        mnode = bs.newnode('math',
                           owner=self.node,
                           attrs={
                               'input1': (0, 1.2, 0),
                               'operation': 'add'
                           })
        self.node.connectattr('torso_position', mnode, 'input2')
        if (rank == 1):
            rank = '\ue01f' + "#" + str(rank) + '\ue01f'
        elif (rank == 2):
            rank = '\ue01f' + "#" + str(rank) + '\ue01f'
        elif (rank == 3):
            rank = '\ue01f' + "#" + str(rank) + '\ue01f'
        else:
            rank = "#" + str(rank)

        self.rank_text = bs.newnode('text',
                                    owner=self.node,
                                    attrs={
                                        'text': rank,
                                        'in_world': True,
                                        'shadow': 1.0,
                                        'flatness': 1.0,
                                        'color': (1, 1, 1),
                                        'scale': 0.01,
                                        'h_align': 'center'
                                    })
        mnode.connectattr('output', self.rank_text, 'position')


class HitPoint(object):
    def __init__(self, position=(0, 1.5, 0), owner=None, prefix='0', shad=1.2):
        self.position = position
        self.node = owner
        m = bs.newnode('math', owner=self.node, attrs={
            'input1': self.position, 'operation': 'add'})
        self.node.connectattr('torso_position', m, 'input2')
        prefix = int(prefix) / 10
        preFix = u"\ue047" + str(prefix) + u"\ue047"
        self._Text = bs.newnode('text',
                                owner=self.node,
                                attrs={
                                    'text': preFix,
                                    'in_world': True,
                                    'shadow': shad,
                                    'flatness': 1.0,
                                    'color': (1, 1, 1) if int(
                                        prefix) >= 20 else (1.0, 0.2, 0.2),
                                    'scale': 0.01,
                                    'h_align': 'center'})
        m.connectattr('output', self._Text, 'position')

        def a():
            self._Text.delete()
            m.delete()

        self.timer = bs.Timer(2, babase.CallStrict(
            a))
