# CacheSCA-Tool Web GUI

基于 Vue 3 + Flask 的 CacheSCA-Tool Web 图形界面，用于测试与评估 openHiTLS 中 AES 与 SM4 性能与对 Cache 类测信道攻击脆弱性。

## 技术栈

### 后端
- **Flask 3.0** - Python Web 框架
- **Flask-CORS** - 跨域支持
- **NumPy** - 数值计算
- **Pandas** - 数据处理

### 前端
- **Vue 3** - 渐进式 JavaScript 框架
- **Vite 5** - 下一代前端构建工具
- **Element Plus** - Vue 3 UI 组件库
- **ECharts** - 数据可视化图表库
- **Pinia** - Vue 状态管理
- **Axios** - HTTP 客户端

## 功能特性

### 1. 主页配置
- 选择加密算法（AES / SM4）
- 选择测试目标（original / preload / constant_time / lut_p / custom）
- 支持自定义测试库上传

### 2. 性能测试
- 在不同系统负载下测试加密性能（Low / Medium / High / Extreme）
- 实时显示性能对比图表
- 支持保存和加载测试结果
- 多组测试结果对比分析

### 3. 安全评估
- Cache 侧信道攻击模拟
- 密钥恢复分析
- 热力图可视化
- 分页查看不同字节索引的分析结果

## 项目结构

```
CacheSCA-Tool/
├── backend/                 # Flask 后端
│   ├── routes/             # API 路由
│   │   ├── config.py       # 配置相关 API
│   │   ├── performance.py  # 性能测试 API
│   │   └── evaluation.py   # 安全评估 API
│   ├── services/           # 业务逻辑
│   │   ├── config_service.py
│   │   ├── performance_service.py
│   │   └── evaluation_service.py
│   ├── app.py              # Flask 应用入口
│   └── requirements.txt    # Python 依赖
│
├── frontend/               # Vue 前端
│   ├── src/
│   │   ├── api/           # API 接口
│   │   ├── stores/        # Pinia 状态管理
│   │   ├── views/         # 页面组件
│   │   │   ├── Home.vue       # 主页
│   │   │   ├── Performance.vue # 性能测试页
│   │   │   └── Evaluation.vue  # 安全评估页
│   │   ├── App.vue        # 根组件
│   │   ├── main.js        # 应用入口
│   │   └── router.js      # 路由配置
│   ├── index.html
│   ├── vite.config.js     # Vite 配置
│   └── package.json       # Node.js 依赖
│
├── start-backend.bat/sh   # 启动后端脚本
└── start-frontend.bat/sh  # 启动前端脚本
```

## 快速开始

### 环境要求

- Python 3.8+
- Node.js 16+
- npm 或 yarn

### 安装与运行


1. **启动后端服务**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

2. **启动前端服务**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### 访问应用

- 前端界面：http://localhost:3000
- 后端 API：http://localhost:5000
- API 健康检查：http://localhost:5000/api/health

## API 文档

### 配置相关

#### GET /api/config/targets
获取指定加密算法的可用测试目标

**参数：**
- `cipher`: 加密算法（AES / SM4）

**响应：**
```json
{
  "targets": ["original", "preload", "constant_time", "lut_p", "custom"]
}
```

#### POST /api/config/set-config
设置当前配置

**请求体：**
```json
{
  "cipher": "AES",
  "target": "original"
}
```

### 性能测试

#### POST /api/performance/test
运行性能测试

**请求体：**
```json
{
  "datafile": "data"
}
```

**响应：**
```json
{
  "success": true,
  "results": {
    "low": 12345,
    "medium": 23456,
    "high": 34567,
    "extreme": 45678
  }
}
```

### 安全评估

#### POST /api/evaluation/test
运行安全评估测试

**请求体：**
```json
{
  "skey": "0b7e151628aed2a6abf7158809cf4f3c",
  "samples": 1000
}
```

#### POST /api/evaluation/heatmap
获取热力图数据

**请求体：**
```json
{
  "index": 0
}
```

## 开发说明

### 前端开发

```bash
cd frontend
npm run dev      # 开发模式
npm run build    # 生产构建
npm run preview  # 预览生产构建
```

### 后端开发

```bash
cd backend
python app.py    # 开发模式（带热重载）
```
