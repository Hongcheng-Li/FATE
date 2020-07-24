#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from pipeline.component.component_base import Component
from pipeline.component.nn.models.sequantial import Sequential
from pipeline.interface.output import Output
from pipeline.utils.tools import extract_explicit_parameter


class HomoNN(Component):
    @extract_explicit_parameter
    def __init__(self, name=None, max_iter=100, batch_size=-1,
                 secure_aggregate=True, aggregate_every_n_epoch=1,
                 early_stop="diff", encode_label=False,
                 predict_param=None, cv_param=None, **kwargs):

        Component.__init__(self, **kwargs["explict_parameters"])

        self.output = Output(self.name, data_type='single')
        self._module_name = "HomoNN"
        self._model = Sequential()
        self.optimizer = None
        self.loss = None
        self.metrics = None
        self.nn_define = None
        self.config_type = "keras"

    def set_model(self, model):
        self._model = model

    def add(self, layer):
        self._model.add(layer)

    def compile(self, optimizer, loss=None, metrics=None):
        if metrics and not isinstance(metrics, list):
            raise ValueError("metrics should be a list")

        self.optimizer = self._model.get_optimizer_config(optimizer)
        self.loss = self._model.get_loss_config(loss)
        self.metrics = metrics
        self.config_type = self._model.get_layer_type()
        self.nn_define = self._model.get_network_config()


