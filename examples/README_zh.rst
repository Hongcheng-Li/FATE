Example Usage Guide
===================

本章节介绍examples目录，它提供了pipeline样例、dsl的配置、
以及正确性对比验证回归的样例、常规建模模版等。
为方便用户快速使用样例，FATE提供样例执行工具`FATE-Test <../python/fate_test/README.rst>`__.

下面将具体介绍主要的功能模块。

FATE-Pipeline
-------------

为了提升联邦建模的易用性，FATE-v1.5 提供了python调用FATE组件的API接口.
用户可通过python编程快速搭建联邦学习模型，具体教程可参考
`FATE-Pipeline <../python/fate_client/pipeline/README.rst>`__.
我们对于每个算法模块也提供了大量的Pipeline搭建联邦学习模型的样例，具体可参考\ `pipeline <./pipeline>`__.

DSL
---

DSL是FATE提供的第一代配置和构建联邦建模任务的方式，具体教程可参考
`DSL配置指引 <../doc/dsl_conf_v2_setting_guide.rst>`__.
在FATE-v1.5版本，我们对DSL进行了全新升级. 主要升级点包括下面几点：

1. 支持按需生成预测DSL，用户可通过FATE-Flow的cli按需生成预测的DSL配置，需要注意的是新版DSL不支持自动预测DSL的生成，用户必须先通过FATE-Flow的cli生成预测DSL，然后再进行预测
2. 支持预测阶段新组件接入，如在预测阶段接入evaluation组件等。
3. 统一算法参数配置风格，role_parameter和algorithm_parameter规范统一

关于最新的DSL各算法组件样例可参考 `dsl/v2 <./dsl/v2>`__\ ，旧的DSL可参考
`dsl/v1 <./dsl/v1>`__\ ，需要注意的是，在FATE-v1.6或者以后的版本里面，旧版本的DSL将会被逐步移除。

Benchmark Quality
-----------------

从FATE-v1.5开始，FATE将提供中心化训练和FATE联邦建模效果的正确性对比工具，用于算法的正确性对比。在v1.5版本中，
我们优先提供了建模中最常用的算法的正确性对比脚本，包括以下模型类型：
* 纵向: LogisticRegression(`benchmark_quality/hetero_lr <./benchmark_quality/hetero_lr>`__),
  SecureBoost(`benchmark_quality/hetero_sbt <./benchmark_quality/hetero_sbt>`__),
  FastSecureBoost(`benchmark_quality/hetero_fast_sbt <./benchmark_quality/hetero_fast_sbt>`__),
  NN(`benchmark_quality/hetero_nn <./benchmark_quality/hetero_nn>`__).
* 横向: LogisticRegression(`benchmark_quality/homo_lr <./benchmark_quality/homo_lr>`__),
  SecureBoost(`benchmark_quality/homo_sbt <./benchmark_quality/homo_sbt>`__), NN(`benchmark_quality/homo_nn <./benchmark_quality/homo_nn>`__.

执行方法可参考\ `benchmark_quality使用文档 <../python/fate_test/README.rst>`__

Upload Default Data
-------------------

FATE
提供了部分公开数据集，存放于\ `data <./data>`__\ 目录下，并为这些数据集提供了一键上传功能。用户可直接使用脚本一键上传所有的内置数据，
或者自定义配置文件，上传自己想要的数据。具体上传方法请参考\ `scripts <./scripts/README.rst>`__

Toy Example
-----------

为了方便用户快速体验FATE开发流程和进行部署检测，FATE提供了简洁的toy任务，具体可参考\ `toy_example <./toy_example/README.md>`__

Min-test
--------

为了方便用户体验建模流程，检测部署完成情况，FATE提供了最小化测试脚本，方便用户一键体验。该脚本将启动纵向逻辑回归和纵向secure_boost算法。用户只需一行启动命令，
配置若干简单参数，即可完成全流程建模。具体使用方法，请参考\ `min_test_task <./min_test_task/README.rst>`__
