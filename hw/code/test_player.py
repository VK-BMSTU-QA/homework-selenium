import pytest
from ui.base_case import BaseCase
from ui.pages.player import Player


class TestPlayer(BaseCase):
    authorize = True

    play_pause_button = Player.player_locators.PLAY_PAUSE_BUTTON
    play_svg =  Player.player_locators.PLAY_SVG
    pause_svg =  Player.player_locators.PAUSE_SVG

    left_button = Player.player_locators.LEFT_BUTTON
    right_button = Player.player_locators.RIGHT_BUTTON
    time = Player.player_locators.TIME

    sound_button = Player.player_locators.SOUND_BUTTON
    full_sound_svg =  Player.player_locators.FULL_SOUND_SVG
    mute_sound_svg =  Player.player_locators.MUTE_SOUND_SVG

    def test_pause_button(self):
        self.player.open_player()
        play_svg = (self.base_page.driver.find_elements_by_xpath(self.play_svg[1])[0])
        pause_svg = (self.base_page.driver.find_elements_by_xpath(self.pause_svg[1])[0])

        play_style = play_svg.get_attribute('style')
        pause_style = pause_svg.get_attribute('style')

        assert pause_style == ''
        assert play_style == 'display: none;'

        self.base_page.click(self.play_pause_button, 20)

        play_svg = (self.base_page.driver.find_elements_by_xpath(self.play_svg[1])[0])
        pause_svg = (self.base_page.driver.find_elements_by_xpath(self.pause_svg[1])[0])

        play_style = play_svg.get_attribute('style')
        pause_style = pause_svg.get_attribute('style')

        assert pause_style == 'display: none;'
        assert play_style == ''

    def test_play_button(self):
        self.player.open_player()
        play_svg = (self.base_page.driver.find_elements_by_xpath(self.play_svg[1])[0])
        pause_svg = (self.base_page.driver.find_elements_by_xpath(self.pause_svg[1])[0])

        play_style = play_svg.get_attribute('style')
        pause_style = pause_svg.get_attribute('style')

        assert pause_style == ''
        assert play_style == 'display: none;'

        self.base_page.click(self.play_pause_button, 20)

        play_svg = (self.base_page.driver.find_elements_by_xpath(self.play_svg[1])[0])
        pause_svg = (self.base_page.driver.find_elements_by_xpath(self.pause_svg[1])[0])

        play_style = play_svg.get_attribute('style')
        pause_style = pause_svg.get_attribute('style')

        assert pause_style == 'display: none;'
        assert play_style == ''

        self.base_page.click(self.play_pause_button, 20)

        play_svg = (self.base_page.driver.find_elements_by_xpath(self.play_svg[1])[0])
        pause_svg = (self.base_page.driver.find_elements_by_xpath(self.pause_svg[1])[0])

        play_style = play_svg.get_attribute('style')
        pause_style = pause_svg.get_attribute('style')

        assert pause_style == ''
        assert play_style == 'display: none;'

    def test_left_button(self):
        self.player.open_player()

        self.base_page.click(self.play_pause_button, 20)

        self.base_page.click(self.right_button, 20)

        time_end = self.base_page.wait_visability_of_elem(self.time)
        time_end_int = int(str(time_end.text)[-2:])

        self.base_page.click(self.left_button, 20)

        time_start = self.base_page.wait_visability_of_elem(self.time)
        time_start_int = int(str(time_start.text)[-2:])

        if time_end_int < 10:
            assert time_start_int - time_end_int <= 50
        else:
            assert time_end_int - time_start_int <= 10

    def test_right_button(self):
        self.player.open_player()

        self.base_page.click(self.play_pause_button, 20)

        time_start = self.base_page.wait_visability_of_elem(self.time)
        time_start_int = int(str(time_start.text)[-2:])

        self.base_page.click(self.right_button, 20)

        time_end = self.base_page.wait_visability_of_elem(self.time)
        time_end_int = int(str(time_end.text)[-2:])

        if time_end_int < 10:
            assert time_start_int - time_end_int <= 50
        else:
            assert time_end_int - time_start_int <= 10

    def test_full_sound_button(self):
        self.player.open_player()
        full_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.full_sound_svg[1])[0])
        mute_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.mute_sound_svg[1])[0])

        full_sound_style = full_sound_svg.get_attribute('style')
        mute_sound_style = mute_sound_svg.get_attribute('style')

        assert full_sound_style == ''
        assert mute_sound_style == 'display: none;'

        self.base_page.click(self.sound_button, 20)

        full_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.full_sound_svg[1])[0])
        mute_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.mute_sound_svg[1])[0])

        full_sound_style = full_sound_svg.get_attribute('style')
        mute_sound_style = mute_sound_svg.get_attribute('style')

        assert full_sound_style == 'display: none;'
        assert mute_sound_style == ''

    def test_mute_sound_button(self):
        self.player.open_player()
        full_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.full_sound_svg[1])[0])
        mute_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.mute_sound_svg[1])[0])

        full_sound_style = full_sound_svg.get_attribute('style')
        mute_sound_style = mute_sound_svg.get_attribute('style')

        assert full_sound_style == ''
        assert mute_sound_style == 'display: none;'

        self.base_page.click(self.sound_button, 20)

        full_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.full_sound_svg[1])[0])
        mute_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.mute_sound_svg[1])[0])

        full_sound_style = full_sound_svg.get_attribute('style')
        mute_sound_style = mute_sound_svg.get_attribute('style')

        assert full_sound_style == 'display: none;'
        assert mute_sound_style == ''

        self.base_page.click(self.sound_button, 20)

        full_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.full_sound_svg[1])[0])
        mute_sound_svg = (self.base_page.driver.find_elements_by_xpath(self.mute_sound_svg[1])[0])

        full_sound_style = full_sound_svg.get_attribute('style')
        mute_sound_style = mute_sound_svg.get_attribute('style')

        assert full_sound_style == ''
        assert mute_sound_style == 'display: none;'