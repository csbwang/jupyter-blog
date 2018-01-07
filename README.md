## 基于pelican搭建的静态博客

### 搭建步骤:
1. clone项目
2. 安装相关依赖: `pip install -r requirements.txt`
3. 安装主题: `git clone --recursive https://github.com/getpelican/pelican-themes.git` 和 `pelican-themes -i themes_namepath/themes_name`
4. 下载插件: `git clone --recursive https://github.com/getpelican/pelican-plugins`
5. 修改配置文件`pelicanconf.py`

### 撰写博文:
通过引入插件，现有配置支持markdown和jupyter notebook两种笔记格式，具体处理如下：
1. 在content目录中新建blog.md或者blog.ipynb(该格式需要同时创建blog.ipynb-meta文件, 用于编辑博文标题、时间、类别和标签等内容)
2. 生成博客(需要创建output目录, 默认生成的博文网页都在改目录中), `make html` / `pelican content`均可
3. 本地预览: `make devserver`(localhost:8000),  预览完成需要手动关闭`make stopserver`
4. 上传至github, `sh tools/update.sh`  
