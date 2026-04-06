# CacheSCA-Tool

## Usage

### Prerequisites

- Python 3.8 or higher
- GCC
- Make
- cpulimit
- stress-ng
- [Modified Mastik](https://github.com/illustager/Mastik)

### 正确性测试

进入测试目录：

```bash
cd CacheSCA-Tool/payload/aes
```

使用既有数据测试对象 `aes_lut_p` 的正确性：

```bash
make run-aes_lut_p data 0 0
```

该程序用法为 `make run-<target> <datafile> <nsamples> <mode>`:

- `target`: 测试对象
  - `original`: AES/SM4 原始实现
  - `aes_lut_p`: AES LUT 实现
  - `aes_preload`: AES 预加载实现
  - `aes_constant_time`: AES 常数时间实现
  - `sm4_lut_p`: SM4 LUT 实现
  - `sm4_preload`: SM4 预加载实现
  - `custom`: 自定义对象。请将想要测试的 `libhitls_crypto.so` 移入 `hitls/custom/` 中。
- `datafile`: 测试数据
- `nsamples`: 测试数据组数（0-自动检测数据组数）
- `mode`: 测试模式（0-正确性测试）

欲测试其它自定义对象，请将对应的 `libhitls_crypto.so` 移入 `hitls/custom/` 中，然后执行：

```bash
make run-custom data 0 0
```

欲重新生成测试用例，执行：

```bash
python generate.py 10000 data
```

该命令在 `data` 文件中生成 10000 组随机用例。

### 性能测试

进入 payload 目录：

```bash
cd CacheSCA-Tool/payload/
```

执行测试脚本 `python payload.py <aim> <cipher> <datafile> <level>`:

- `aim`: 测试对象
- `cipher`: 算法（aes/sm4）
- `datafile`: 测试数据，同**安全性测试**
- `level`: 系统负载（low/medium/high/extreme）

如：

```bash
python payload.py aes_lut_p aes data high
```

输出为所用时钟周期数。

### 安全评估

进入 evaluation 目录：

```bash
cd CacheSCA-Tool/payload/evaluation
```

执行测试 `make run-<cipher>-<target> [ARGS="-k <key> -s <nsamples>"] > results`:

- `cipher`: 算法（aes/sm4）
- `target`: 测试对象
- `key`: 测试密钥
- `nsamples`: 采样组数

如：

```bash
make run-aes-aes_lut_p > results
```

分析输出：

```bash
python analyze.py results
```
