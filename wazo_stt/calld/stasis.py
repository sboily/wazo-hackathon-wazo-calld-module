# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

logger = logging.getLogger(__name__)


class SttStasis:

    def __init__(self, config, ari, stt_service):
        self.config = config
        self._ari = ari.client
        self._stt_service = stt_service

    def initialize(self):
        if self.config["stt"]["stasis"]:
            self._ari.on_channel_event('StasisStart', self._stasis_start)
            logger.debug('Stasis stt initialized')

    def _stasis_start(self, event_objects, event):
        logger.critical("event_objects: %s", event_objects)
        logger.critical("event: %s", event)
        channel = event_objects["channel"]
        self._stt_service.start(channel)
        logger.critical("thread started")
