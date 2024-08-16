from prints import *


def GlassToPanel(Dye, NeedPanel):
    if Dye == None:
        used_glass = 0
        have_panels = 0
        while have_panels < NeedPanel:
            used_glass += 6
            have_panels += 16
        print(f'Необходимо стекла: {used_glass} ед. {used_glass // 64}+{used_glass % 64}')
        if have_panels > NeedPanel:
            print(
                f'Перекрафт панелей: {have_panels - NeedPanel} ед., {int(100 // (have_panels / (have_panels - NeedPanel)))}%')
    if Dye == 1:
        lost_coler_glass = 0
        used_glass = 0
        used_dye = 0
        have_panels = 0
        while have_panels < NeedPanel:
            if lost_coler_glass >= 6:
                lost_coler_glass -= 6
                have_panels += 16
            else:
                used_glass += 8
                used_dye += 1
                lost_coler_glass += 8
        print(f'Необходимо стекла: {used_glass} ед. {used_glass // 64}+{used_glass % 64}')
        print(f'Необходимо красителя: {used_dye} ед. {used_dye // 64}+{used_dye % 64}')
        if have_panels > NeedPanel:
            print(
                f'Перекрафт панелей: {have_panels - NeedPanel} ед., {int(100 // (have_panels / (have_panels - NeedPanel)))}%')


def PanelCraft():
    AllDye()
    Selected_dye = int(input())
    print('Сколько необходимо Панелей?')
    ResultePanel = int(input())

    if Selected_dye == 1:
        GlassToPanel(None, ResultePanel)
    if Selected_dye != 1:
        GlassToPanel(1, ResultePanel)


def GlassCraft():
    AllDye()
    Selected_dye = int(input())
    print('Сколько необходимо Стекла?')
    ResulteGlass = int(input())
    if Selected_dye == 1:
        print(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    if Selected_dye != 1:
        used_glass = 0
        used_dye = 0
        while used_glass < ResulteGlass:
            used_glass += 8
            used_dye += 1
        print(f'Необходимо стекла: {used_glass} ед. {used_glass // 64}+{used_glass % 64}')
        print(f'Необходимо красителя: {used_dye} ед. {used_dye // 64}+{used_dye % 64}')
