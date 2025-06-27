# Author: 邵世昌
# CreateTime: 2025/6/26
# FileName: 数据分析系统
import streamlit as st
import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta
import altair as alt
import mysql.connector
from streamlit_option_menu import option_menu
import json
import hashlib
import os
import base64
import re
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_autorefresh import st_autorefresh
# 确保中文和负号正常显示
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 页面配置
st.set_page_config(layout="wide", page_title="数据分析系统")

# 自定义CSS设置背景图
def set_bg_image(url):
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url({url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 使用示例图片URL，实际使用时替换为你的图片URL
# set_bg_image("https://img.picui.cn/free/2025/06/25/685bc513d6d52.jpeg")

# 存储配置
STORAGE_DIR = ".streamlit_auth"
AUTH_FILE = os.path.join(STORAGE_DIR, "auth.json")


# 创建存储目录
def create_storage_dir():
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

# 安全存储凭证
def save_credentials(username, password_hash):
    create_storage_dir()
    expiry = (datetime.now() + timedelta(days=30)).isoformat()

    # 加密存储（Base64编码）
    encoded_username = base64.b64encode(username.encode()).decode()
    encoded_hash = base64.b64encode(password_hash.encode()).decode()

    data = {
        "username": encoded_username,
        "password_hash": encoded_hash,
        "expiry": expiry
    }

    with open(AUTH_FILE, 'w') as f:
        json.dump(data, f)


# 加载凭证
def load_credentials():
    if not os.path.exists(AUTH_FILE):
        return None, None

    try:
        with open(AUTH_FILE, 'r') as f:
            data = json.load(f)

        # 检查凭证是否过期
        expiry = datetime.fromisoformat(data['expiry'])
        if datetime.now() > expiry:
            os.remove(AUTH_FILE)
            return None, None

        # 解密
        username = base64.b64decode(data['username']).decode()
        password_hash = base64.b64decode(data['password_hash']).decode()

        return username, password_hash
    except:
        os.remove(AUTH_FILE)
        return None, None


# 删除凭证
def delete_credentials():
    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)


# 密码哈希
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# 数据文件路径
USERS_FILE = "users.json"
LOG_FILE = "日志.log"


# 从文件加载用户数据
def load_users_from_file():
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 返回初始用户
        return [
            {
                "邵世昌": {
                    "password": "do1ssc2025.",
                    "role": "admin",
                    "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        ]


# 将用户数据保存到文件
def save_users_to_file():
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(st.session_state.users, f, ensure_ascii=False, indent=4)


# 从文件加载历史日志
def load_logs_from_file():
    try:
        logs = []
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(' - ', 3)
                if len(parts) == 4:
                    timestamp, username, module, action = parts
                    logs.append({
                        "timestamp": timestamp,
                        "username": username,
                        "module": module,
                        "action": action
                    })
        return logs
    except FileNotFoundError:
        return []


# 初始化会话状态中的用户和日志
if 'users' not in st.session_state:
    st.session_state.users = load_users_from_file()

if 'logs' not in st.session_state:
    st.session_state.logs = load_logs_from_file()


def login_page():
    """创建Streamlit登录页面"""
    # 自定义CSS居中标题
    st.markdown("""
        <style>
            .title {
                text-align: center;
                margin-bottom: 30px;
            }
            .form-container {
                max-width: 400px;
                margin: 0 auto;
            }
        </style>
    """, unsafe_allow_html=True)

    # 登录表单
    with st.container(border=True):
        with st.form(key='login_form', clear_on_submit=True):
            st.markdown("<h1 style='text-align: center; margin-bottom: 20px;'>系统登录</h1>", unsafe_allow_html=True)

            # 用户名输入 - 新增自动填充
            saved_username, _ = load_credentials()
            username = st.text_input(
                "账号",
                placeholder="请输入账号",
                key="login_username",
                value=saved_username or "",
                help="请输入注册的用户名"
            )

            # 密码输入
            password = st.text_input(
                "密码",
                type="password",
                placeholder="请输入密码",
                key="login_password",
                help="请输入与账号匹配的密码"
            )

            # 记住我选项 - 增强功能
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                # 加载记住状态
                saved_remember = load_credentials() is not None
                remember_me = st.checkbox("记住我", key="remember_me", value=saved_remember)
            with col2:
                st.empty()
            with col3:
                st.write("如有疑问，请联系邵世昌！！！")

            # 登录按钮
            login_button = st.form_submit_button(
                label="登录",
                type="primary",
                help="点击此按钮登录系统",
                use_container_width=True
            )

            if login_button:
                # 登录验证
                if not username or not password:
                    st.error("账号和密码不能为空")
                    return

                for user in st.session_state.users:
                    if username in user and user[username]["password"] == password:
                        st.session_state['authenticated'] = True
                        st.session_state['username'] = username
                        st.session_state['remember'] = remember_me
                        st.session_state['role'] = user[username]["role"]  # 记录用户角色

                        # 处理记住我选项
                        if remember_me:
                            password_hash = hash_password(password)
                            save_credentials(username, password_hash)
                            st.success("已记住您的登录状态，下次将自动登录")
                        else:
                            delete_credentials()

                        # 记录登录日志
                        log_action(f"用户 {username} 执行登录操作", "认证模块")
                        st.success("登录成功！正在跳转...", icon="✅")
                        st.balloons()
                        time.sleep(2)
                        st.rerun()
                        return

                st.error("账号或密码错误，请重新输入", icon="❌")


def log_action(action, module="系统模块"):
    """记录详细操作日志"""
    # 处理未登录状态
    username = st.session_state.get('username', '匿名用户')
    # 生成日志条目
    log_entry = {
        "username": username,
        "action": action,
        "module": module,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    st.session_state.logs.append(log_entry)

    # 将日志写入文件
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        log_str = f"{log_entry['timestamp']} - {log_entry['username']} - {log_entry['module']} - {log_entry['action']}\n"
        f.write(log_str)


# 日志查看
def log_viewer():
    """日志查看模块，展示所有用户操作记录"""
    st.subheader("访问日志", anchor="log-viewer")

    # 获取所有用户列表用于筛选
    if st.session_state.logs:
        all_users = sorted(list(set(log["username"] for log in st.session_state.logs)))
    else:
        all_users = []

    # 创建用户筛选器
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_users = st.multiselect(
            "用户筛选",
            options=all_users,
            default=all_users,
            key="log_user_filter"
        )
    with col2:
        st.write("")  # 占位符，用于对齐
        if st.button("重置筛选", key="reset_log_filter"):
            selected_users = all_users

    # 筛选日志
    filtered_logs = [
        log for log in st.session_state.logs
        if log["username"] in selected_users
    ]

    # 显示日志表格
    logs_df = pd.DataFrame(filtered_logs)
    if not logs_df.empty:
        # 优化表格显示
        st.dataframe(
            logs_df,
            use_container_width=True,
            column_config={
                "username": st.column_config.TextColumn("操作用户", width="medium"),
                "action": st.column_config.TextColumn("操作内容", width="large"),
                "module": st.column_config.TextColumn("模块", width="small"),
                "timestamp": st.column_config.DatetimeColumn("时间戳", width="small")
            }
        )
    else:
        st.info("暂无符合条件的日志记录", icon="ℹ️")


# 用户管理
def user_management():
    st.subheader("用户管理", anchor="user-management")

    # 使用选项卡组织界面
    tab1, tab2, tab3, tab4 = st.tabs(["添加用户", "删除用户", "修改用户信息", "查看用户"])

    with tab1:
        # 添加用户
        st.markdown("### 添加新用户")
        new_username = st.text_input("新用户名", key="new_username")
        new_password = st.text_input("新用户密码", type="password", key="new_password")
        new_role = st.selectbox("新用户角色", ["admin", "user"], key="new_role")

        if st.button("添加用户", key="add_user_button", use_container_width=True):
            if new_username and new_password:
                # 检查用户名是否已存在
                existing_usernames = [list(user.keys())[0] for user in st.session_state.users]
                if new_username in existing_usernames:
                    st.error("用户名已存在，请选择其他用户名", icon="❌")
                else:
                    create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_user = {new_username: {"password": new_password, "role": new_role, "create_time": create_time}}
                    st.session_state.users.append(new_user)
                    save_users_to_file()  # 保存用户数据到文件
                    log_action(f"添加新用户 {new_username}", "用户管理模块")
                    st.success(f"用户 {new_username} 添加成功！", icon="✅")
            else:
                st.error("用户名和密码不能为空", icon="❌")

    with tab2:
        # 删除用户
        st.markdown("### 删除现有用户")
        existing_usernames = [list(user.keys())[0] for user in st.session_state.users]

        # 检查是否有用户可删除
        if not existing_usernames:
            st.info("当前没有用户可删除", icon="ℹ️")
        else:
            user_to_delete = st.selectbox("选择要删除的用户", existing_usernames, key="user_to_delete")
            if st.button("确认删除", key="delete_user_button", use_container_width=True):
                # 防止删除最后一个管理员
                if len(existing_usernames) == 1 and st.session_state.users[0][user_to_delete]["role"] == "admin":
                    st.error("不能删除唯一的管理员用户", icon="❌")
                else:
                    for user in st.session_state.users:
                        if user_to_delete in user:
                            st.session_state.users.remove(user)
                            save_users_to_file()  # 保存用户数据到文件
                            log_action(f"删除用户 {user_to_delete}", "用户管理模块")
                            st.success(f"用户 {user_to_delete} 删除成功！", icon="✅")
                            break

    with tab3:
        # 修改用户信息
        st.markdown("### 修改用户信息")
        existing_usernames = [list(user.keys())[0] for user in st.session_state.users]

        # 检查是否有用户可修改
        if not existing_usernames:
            st.info("当前没有用户可修改信息", icon="ℹ️")
        else:
            user_to_modify = st.selectbox("选择要修改信息的用户", existing_usernames, key="user_to_modify")
            new_password_modify = st.text_input("新密码（留空则不修改）", type="password", key="new_password_modify")
            new_role_modify = st.selectbox("新角色", ["admin", "user"], key="new_role_modify")

            # 显示当前用户信息
            current_user_info = next(user for user in st.session_state.users if user_to_modify in user)[user_to_modify]
            st.markdown(f"**当前信息**：角色 - {current_user_info['role']}")

            if st.button("确认修改", key="modify_user_button", use_container_width=True):
                for user in st.session_state.users:
                    if user_to_modify in user:
                        if new_password_modify:
                            user[user_to_modify]["password"] = new_password_modify
                        user[user_to_modify]["role"] = new_role_modify
                        save_users_to_file()  # 保存用户数据到文件
                        log_action(f"修改用户 {user_to_modify} 的信息", "用户管理模块")
                        st.success(f"用户 {user_to_modify} 的信息修改成功！", icon="✅")
                        break

    with tab4:
        # 查看用户
        st.markdown("### 当前用户列表")

        # 检查是否有用户
        if not st.session_state.users:
            st.info("当前系统中没有用户", icon="ℹ️")
        else:
            # 准备数据用于表格显示
            user_data = []
            for user_dict in st.session_state.users:
                username = list(user_dict.keys())[0]
                user_info = user_dict[username]
                user_data.append({
                    "用户名": username,
                    "角色": user_info["role"],
                    "创建时间": user_info.get("create_time", "未知")
                })

            # 创建DataFrame并显示
            user_df = pd.DataFrame(user_data)

            # 按创建时间排序（最新创建的在前面）
            if "创建时间" in user_df.columns and user_df["创建时间"].iloc[0] != "未知":
                user_df = user_df.sort_values(by="创建时间", ascending=False)

            # 使用Streamlit的dataframe组件显示用户信息
            st.dataframe(
                user_df,
                column_config={
                    "用户名": st.column_config.TextColumn("用户名", width="medium"),
                    "角色": st.column_config.SelectboxColumn("角色", options=["admin", "user"], width="small"),
                    "创建时间": st.column_config.DatetimeColumn("创建时间", format="YYYY-MM-DD HH:mm:ss",
                                                                width="medium")
                },
                hide_index=True,
            )

            # 显示用户统计信息
            total_users = len(user_df)
            admin_count = len(user_df[user_df["角色"] == "admin"])
            user_count = len(user_df[user_df["角色"] == "user"])

            col1, col2, col3 = st.columns(3)
            col1.metric("总用户数", total_users)
            col2.metric("管理员数", admin_count)
            col3.metric("普通用户数", user_count)


# 导入本地数据
def get_local_data():
    # 侧边栏
    with st.sidebar:
        # 文件上传器
        uploaded_file = st.file_uploader(
            "",
            type=["csv", "xlsx", "xls"],
            accept_multiple_files=False,
            key="market_data_upload",
            label_visibility="collapsed"
        )

        # 上传按钮
        if st.button("导入数据", key="import_data_btn",use_container_width = True) and uploaded_file is not None:
            log_action(f"用户上传了数据：{uploaded_file.name}", "上传模块")
            try:
                # 显示加载状态
                with st.spinner("正在处理数据..."):
                    # 根据文件类型读取数据
                    if uploaded_file.name.endswith('.csv'):
                        data = pd.read_csv(uploaded_file)
                    else:
                        data = pd.read_excel(uploaded_file)

                    # 保存数据到session_state供后续页面使用
                    st.session_state['market_data'] = data
                    # 设置数据导入标志
                    st.session_state['data_imported'] = True

                    # 显示成功消息
                    st.success(f"数据导入成功，共 {len(data)} 行记录")
            except Exception as e:
                st.error(f"导入失败: {str(e)}")
                # 导入失败时清除数据标志
                st.session_state['data_imported'] = False

# 市场部
def dashboard_page_market():
    get_local_data()

# 公有云
def dashboard_page_saas():
    get_local_data()

# 事业一部
def dashboard_page_one():
    # 连接数据库获取数据
    # try:
    #     conn = mysql.connector.connect(
    #         host="192.168.83.21",
    #         user="saasdata",
    #         password="Do1admin_123",
    #         database="do1data"
    #     )
    #     data = conn.cursor.execute("""SELECT *  FROM TABLE""")
    #     print(f"MySQL 连接成功 | 版本: {conn.get_server_info()}")
    # except Exception as e:
    #     print(f"连接失败: {e}")
    # finally:
    #     conn.close() if conn else None
    get_local_data()  # 上传数据
    st_autorefresh(interval=600000, limit=None) # 页面自动刷新每小时刷新一次
    @st.cache_data() # 缓存数据
    def load_date():
        df_one = st.session_state.get('market_data', pd.DataFrame())
        return df_one
    df_one = load_date()
    if df_one.empty:
        st.stop()  # 避免初始化报错
    df_one["所属年度"] = pd.to_datetime(df_one["所属年度"])
    df_one["客户发起需求日期"] = pd.to_datetime(df_one["客户发起需求日期"])
    df_one["销售跟进日期"] = pd.to_datetime(df_one["销售跟进日期"])
    df_one['成交日期'] = pd.to_datetime(df_one['成交日期'])
    df_one['创建时间'] = pd.to_datetime(df_one['创建时间'])
    if df_one.empty:
        st.warning("无有效数据！！！")
        st.stop()

    # ***********数据概览***********
    non_nat_data = df_one[df_one['客户发起需求日期'].notna()]
    if not non_nat_data.empty:
        start_date = non_nat_data['客户发起需求日期'].min().strftime('%Y-%m-%d')
        end_date = non_nat_data['客户发起需求日期'].max().strftime('%Y-%m-%d')
        data_range_info = f"数据范围: {start_date} 至 {end_date}\n\n"
    else:
        data_range_info = "数据中无有效客户发起需求日期\n\n"
    st.sidebar.info(
        data_range_info +
        f"总线索数: {len(df_one):,}\n\n"
        f"客户来源数: {len(df_one['客户来源'].unique())}\n\n"
        f"销售跟进人数: {len(df_one['销售跟进人'].unique())}\n\n"
        f"一级行业数: {len(df_one['一级行业'].unique())}\n\n"
        f"二级行业数: {len(df_one['二级行业'].unique())}"
    )
    Col1, Col2, Col3 = st.columns([2, 5, 2])
    with Col1:
        # 企业地区分布
        with st.container():
            # 增强版地区匹配正则表达式
            region_patterns = {
                "华东": re.compile(r"华东|上海|南京|无锡|徐州|常州|苏州|南通|连云港|淮安|盐城|扬州|镇江|泰州|宿迁|"
                                   r"杭州|宁波|温州|嘉兴|湖州|绍兴|金华|衢州|舟山|台州|丽水|合肥|芜湖|蚌埠|淮南|马鞍山|"
                                   r"淮北|铜陵|安庆|黄山|滁州|阜阳|宿州|巢湖|六安|亳州|池州|宣城|福州|厦门|莆田|三明|"
                                   r"泉州|漳州|南平|龙岩|宁德|南昌|景德镇|萍乡|九江|新余|鹰潭|赣州|吉安|宜春|抚州|上饶|"
                                   r"济南|青岛|淄博|枣庄|东营|烟台|潍坊|济宁|泰安|威海|日照|莱芜|临沂|德州|聊城|滨州|菏泽",
                                   re.IGNORECASE),
                "华南": re.compile(r"华南|广东|广州|深圳|珠海|汕头|佛山|韶关|湛江|肇庆|江门|茂名|惠州|梅州|汕尾|河源|"
                                   r"阳江|清远|东莞|中山|潮州|揭阳|云浮|广西|南宁|柳州|桂林|梧州|北海|防城港|钦州|贵港|"
                                   r"玉林|百色|贺州|河池|来宾|崇左|海南|海口|三亚|三沙|儋州", re.IGNORECASE),
                "华北": re.compile(r"华北|北京|天津|河北|石家庄|唐山|秦皇岛|邯郸|邢台|保定|张家口|承德|沧州|廊坊|衡水|"
                                   r"山西|太原|大同|阳泉|长治|晋城|朔州|晋中|运城|忻州|临汾|吕梁|内蒙古|呼和浩特|包头|乌海|"
                                   r"赤峰|通辽|鄂尔多斯|呼伦贝尔|巴彦淖尔|乌兰察布|兴安|锡林郭勒|阿拉善",
                                   re.IGNORECASE),
                "华中": re.compile(r"华中|河南|郑州|开封|洛阳|平顶山|安阳|鹤壁|新乡|焦作|濮阳|许昌|漯河|三门峡|南阳|商丘|"
                                   r"信阳|周口|驻马店|湖北|武汉|黄石|十堰|宜昌|襄阳|鄂州|荆门|孝感|荆州|黄冈|咸宁|随州|恩施|"
                                   r"湖南|长沙|株洲|湘潭|衡阳|邵阳|岳阳|常德|张家界|益阳|郴州|永州|怀化|娄底|湘西",
                                   re.IGNORECASE),
                "西北": re.compile(r"西北|陕西|西安|铜川|宝鸡|咸阳|渭南|延安|汉中|榆林|安康|商洛|甘肃|兰州|嘉峪关|金昌|白银|"
                                   r"天水|武威|张掖|平凉|酒泉|庆阳|定西|陇南|临夏|甘南|青海|西宁|海东|海北|黄南|海南|果洛|玉树|海西|"
                                   r"宁夏|银川|石嘴山|吴忠|固原|中卫|新疆|乌鲁木齐|克拉玛依|吐鲁番|哈密|昌吉|博尔塔拉|巴音郭楞|阿克苏|"
                                   r"克孜勒苏柯尔克孜|喀什|和田|伊犁|塔城|阿勒泰", re.IGNORECASE),
                "西南": re.compile(r"西南|重庆|四川|成都|自贡|攀枝花|泸州|德阳|绵阳|广元|遂宁|内江|乐山|南充|眉山|宜宾|广安|达州|"
                                   r"雅安|巴中|资阳|阿坝|甘孜|凉山|贵州|贵阳|六盘水|遵义|安顺|毕节|铜仁|黔西南|黔东南|黔南|云南|昆明|"
                                   r"曲靖|玉溪|保山|昭通|丽江|普洱|临沧|楚雄|红河|文山|西双版纳|大理|德宏|怒江|迪庆|西藏|拉萨|日喀则|"
                                   r"昌都|林芝|山南|那曲|阿里", re.IGNORECASE),
                "东北": re.compile(r"东北|辽宁|沈阳|大连|鞍山|抚顺|本溪|丹东|锦州|营口|阜新|辽阳|盘锦|铁岭|朝阳|葫芦岛|吉林|长春|"
                                   r"吉林|四平|辽源|通化|白山|松原|白城|延边|黑龙江|哈尔滨|齐齐哈尔|鸡西|鹤岗|双鸭山|大庆|伊春|佳木斯|"
                                   r"七台河|牡丹江|黑河|绥化|大兴安岭", re.IGNORECASE)
            }

            def get_region(company_name):
                # 处理非字符串值
                if not isinstance(company_name, str):
                    company_name = str(company_name)  # 转换为字符串
                    if company_name.lower() == 'nan':  # 处理NaN值
                        return "其他"

                # 执行正则匹配
                for region, pattern in region_patterns.items():
                    if pattern.search(company_name):
                        return region
                return "其他"

            # 地区颜色映射（保持视觉一致性）
            region_colors = {
                "华东": "#3498db",  # 蓝色
                "华南": "#e74c3c",  # 红色
                "华北": "#2ecc71",  # 绿色
                "东北": "#9b59b6",  # 紫色
                "西南": "#e67e22",  # 橙色
                "西北": "#f1c40f",  # 黄色
                "华中": "#1abc9c",  # 青色
                "其他": "#bdc3c7"  # 灰色
            }
            # 新增一列存储地区信息
            df_one["地区"] = df_one["企业名称"].apply(get_region)

            # 统计各地区企业数量
            region_counts = df_one["地区"].value_counts().reset_index()
            region_counts.columns = ["地区", "数量"]

            # 按预设顺序排序
            ordered_regions = ["华东", "华南", "华北", "东北", "西南", "西北", "华中", "其他"]
            region_counts["地区"] = pd.Categorical(region_counts["地区"], categories=ordered_regions, ordered=True)
            region_counts = region_counts.sort_values("地区").dropna()

            # 使用 Seaborn 绘制美观的柱状图
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(
                x="地区",
                y="数量",
                data=region_counts,
                palette=[region_colors.get(region, "#bdc3c7") for region in region_counts["地区"]],
                ax=ax
            )

            # 添加数据标签
            for p in ax.patches:
                ax.annotate(
                    f'{int(p.get_height())}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center',
                    va='center',
                    fontsize=12,
                    color='black',
                    xytext=(0, 5),
                    textcoords='offset points'
                )

            # 设置图表样式
            ax.set_title("企业地区分布", fontsize=16, pad=20)
            ax.set_xlabel("地区", fontsize=14, labelpad=10)
            ax.set_ylabel("企业数量", fontsize=14, labelpad=10)
            ax.tick_params(axis='both', which='major', labelsize=12)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='y', linestyle='--', alpha=0.7)

            # 显示图表
            st.pyplot(fig)  # 企业地区分布
    with Col2:
        # 数据大屏指标卡片
        with st.container():
            # 定义轻量化样式
            st.markdown("""
            <style>

                /* 若想全局居中所有 radio，直接用 .stRadio */
                .stRadio {
                    display: flex;
                    justify-content: center;
                    margin-bottom: 0px !important;
                    margin-top: -40px !important;
                    align-items: center;
                    text-align: center; 
                }

                /* 压缩 selectbox 组件的下边距 */
                .stSelectbox {
                    margin-top: -20px !important;
                    margin-bottom: -20px !important;     /* 拉近与 radio 的距离 */
                }

                /* 全局样式 */
                .dashboard-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 4px;
                    margin: 0;
                    padding: 0;
                }

                /* 指标卡片样式 */
                .metric-card {
                    margin-top: 0px !important;
                    margin-bottom: -30px !important;
                    background-color: #f0f2f6;
                    border-radius: 0px;
                    padding: 0px;
                    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
                    flex: 1 1 calc(25% - 12px);
                    min-width: 100px;
                    display: flex;
                    flex-direction: column;
                    transition: box-shadow 0.3s ease;
                    flex-direction: column; /* 让子元素垂直排列 */
                    justify-content: center; /* 垂直方向居中 */
                    align-items: center; /* 水平方向居中 */
                    text-align: center; /* 文字自身也居中（比如标题、数值等 inline 元素） */
                }

                .metric-card:hover {
                    box-shadow: 0 0px 0px rgba(0,0,0,0.12);
                }

                /* 卡片标题 */
                .card-title {
                    font-size: 14px;
                    font-weight: 600;
                    color: #4a5568;
                    margin-bottom: 0px;
                    display: flex;
                    align-items: center;
                }

                /* 卡片数值 */
                .card-value {
                    font-size: 24px;
                    font-weight: 700;
                    color: #1a202c;
                    margin: 0px;
                    flex-grow: 1;
                    display: flex;
                    align-items: flex-end;
                }

                /* 变化率 */
                .card-delta {
                    font-size: 12px;
                    display: flex;
                    align-items: center;
                    margin-top: 0px;
                }

                .delta-up {
                    color: #2b6cb0;
                    display: flex;
                    align-items: center;
                }

                .delta-down {
                    color: #e53e3e;
                    display: flex;
                    align-items: center;
                }

                .delta-neutral {
                    color: #718096;
                    display: flex;
                    align-items: center;
                }

                /* 时间段选择器 */
                .time-selector {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0px;
                    margin-bottom: 0px;
                    background-color: #f0f2f6;
                    border-radius: 0px;
                    padding: 0px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                }

                /* 响应式调整 - 小屏显示2列 */
                @media (max-width: 768px) {
                    .metric-card {
                        flex: 1 1 calc(50% - 12px);
                    }
                }
            </style>
            """, unsafe_allow_html=True)

            # # 主页面区域显示数据预览
            # if st.session_state.get('data_imported', False):
            #     if st.checkbox("数据预览", key="preview_checkbox"):
            #         # 创建一个滑块让用户选择要显示的行数
            #         preview_rows = st.slider(
            #             "选择要显示的行数",
            #             min_value=1,
            #             max_value=len(st.session_state['market_data']),
            #             value=10,
            #             step=1
            #         )
            #         # 显示指定行数的数据预览
            #         st.dataframe(st.session_state['market_data'].head(preview_rows))

            # 时间段选择 - 第一部分
            time_period_col1, time_period_col2 = st.columns(2)

            # 获取数据时间范围
            min_date = df_one['创建时间'].min()
            max_date = df_one['创建时间'].max()

            # 生成时间范围
            available_months = [max_date.to_period('M') - i for i in range(12)]
            available_years = list(range(min_date.year, max_date.year + 1))

            # 第一个时间段选择
            with time_period_col1:
                period1_type = st.radio(
                    "",
                    ["本月", "上月", "指定月", "指定年"],
                    index=0,
                    key="p1_type_compact",
                    horizontal=True,
                    label_visibility="collapsed"
                )
                if period1_type == "指定月":
                    period1_month = st.selectbox(
                        "", ["选择月"] + available_months[:11],
                        index=1, key="p1_month_compact",
                        label_visibility="collapsed"
                    )
                    period1_name = f"{period1_month}"
                    period1_data = df_one[df_one['创建时间'].dt.to_period('M') == period1_month]
                elif period1_type == "指定年":
                    period1_year = st.selectbox(
                        "", ["选择年"] + available_years,
                        index=len(available_years), key="p1_year_compact",
                        label_visibility="collapsed"
                    )
                    period1_name = f"{period1_year}年"
                    period1_data = df_one[df_one['创建时间'].dt.year == period1_year]
                else:
                    period1_month = max_date.to_period('M') - (1 if period1_type == "上月" else 0)
                    period1_name = f"{period1_month}"
                    period1_data = df_one[df_one['创建时间'].dt.to_period('M') == period1_month]

            # 第二个时间段选择
            with time_period_col2:
                period2_type = st.radio(
                    "",
                    ["上月", "去年同期", "指定月", "指定年"],
                    index=0,
                    key="p2_type_compact",
                    horizontal=True,
                    label_visibility="collapsed"
                )
                if period2_type == "指定月":
                    period2_month = st.selectbox(
                        "", ["选择月"] + available_months[:11],
                        index=2, key="p2_month_compact",
                        label_visibility="collapsed"
                    )
                    period2_name = f"{period2_month}"
                    period2_data = df_one[df_one['创建时间'].dt.to_period('M') == period2_month]
                elif period2_type == "指定年":
                    period2_year = st.selectbox(
                        "", ["选择年"] + available_years,
                        index=len(available_years) - 1 if len(available_years) > 1 else 0,
                        key="p2_year_compact",
                        label_visibility="collapsed"
                    )
                    period2_name = f"{period2_year}年"
                    period2_data = df_one[df_one['创建时间'].dt.year == period2_year]
                else:
                    if period2_type == "去年同期" and period1_type in ["本月", "上月", "指定月"]:
                        period2_month = period1_month - 12
                        period2_name = f"{period2_month}"
                        period2_data = df_one[df_one['创建时间'].dt.to_period('M') == period2_month]
                    else:
                        period2_month = max_date.to_period('M') - 1
                        period2_name = f"{period2_month}"
                        period2_data = df_one[df_one['创建时间'].dt.to_period('M') == period2_month]

            st.markdown('</div>', unsafe_allow_html=True)  # 结束时间段选择

            # 计算指标函数
            def calc_metrics(d):
                t = len(d);
                c = len(d[d['是否成交'] == '是'])
                r = round(c / t * 100, 2) if t > 0 else 0
                a = d['合同金额'].sum()
                return t, c, r, a

            # 计算指标
            p1_l, p1_c, p1_r, p1_a = calc_metrics(period1_data)
            p2_l, p2_c, p2_r, p2_a = calc_metrics(period2_data)

            # 计算变化率
            def change(c, p):
                return round((c - p) / p * 100, 2) if p > 0 else 0

            # 第一列卡片容器
            with st.container():
                col1, col2, col3, col4 = st.columns(4)

                # 总线索数卡片
                with col1:
                    st.markdown('''
                    <div class="metric-card">
                        <p class="card-title">📊 总线索数</p>
                        <p class="card-value">{p1_l:,}</p>
                        <p class="card-delta {cls}">{dir} {chg}%</p>
                    </div>
                    '''.format(
                        p1_l=p1_l,
                        chg=change(p1_l, p2_l),
                        cls='delta-up' if change(p1_l, p2_l) > 0 else 'delta-down' if change(p1_l,
                                                                                             p2_l) < 0 else 'delta-neutral',
                        dir='↑' if change(p1_l, p2_l) > 0 else '↓' if change(p1_l, p2_l) < 0 else '→'
                    ), unsafe_allow_html=True)

                # 成交线索数卡片
                with col2:
                    st.markdown('''
                    <div class="metric-card">
                        <p class="card-title">🎯 成交线索</p>
                        <p class="card-value">{p1_c:,}</p>
                        <p class="card-delta {cls}">{dir} {chg}%</p>
                    </div>
                    '''.format(
                        p1_c=p1_c,
                        chg=change(p1_c, p2_c),
                        cls='delta-up' if change(p1_c, p2_c) > 0 else 'delta-down' if change(p1_c,
                                                                                             p2_c) < 0 else 'delta-neutral',
                        dir='↑' if change(p1_c, p2_c) > 0 else '↓' if change(p1_c, p2_c) < 0 else '→'
                    ), unsafe_allow_html=True)

                # 成交率卡片
                with col3:
                    st.markdown('''
                    <div class="metric-card">
                        <p class="card-title">📈 成交率</p>
                        <p class="card-value">{p1_r:.1f}%</p>
                        <p class="card-delta {cls}">{dir} {chg:.1f}%</p>
                    </div>
                    '''.format(
                        p1_r=p1_r,
                        chg=p1_r - p2_r,
                        cls='delta-up' if p1_r > p2_r else 'delta-down' if p1_r < p2_r else 'delta-neutral',
                        dir='↑' if p1_r > p2_r else '↓' if p1_r < p2_r else '→'
                    ), unsafe_allow_html=True)

                # 合同金额卡片
                with col4:
                    st.markdown('''
                    <div class="metric-card">
                        <p class="card-title">💰 合同金额</p>
                        <p class="card-value">¥{p1_a:,.1f}</p>
                        <p class="card-delta {cls}">{dir} {chg}%</p>
                    </div>
                    '''.format(
                        p1_a=p1_a,
                        chg=change(p1_a, p2_a),
                        cls='delta-up' if change(p1_a, p2_a) > 0 else 'delta-down' if change(p1_a,
                                                                                             p2_a) < 0 else 'delta-neutral',
                        dir='↑' if change(p1_a, p2_a) > 0 else '↓' if change(p1_a, p2_a) < 0 else '→'
                    ), unsafe_allow_html=True)
            # 第二列卡片容器
            with st.container():
                col1, col2, col3, col4 = st.columns(4)

                # 对比总线索数卡片
                with col1:
                    st.markdown('''
                    <div class="metric-card compare">
                        <p class="card-title">{p2_name} 总线索数</p>
                        <p class="card-value">{p2_l:,}</p>
                    </div>
                    '''.format(p2_name=period2_name, p2_l=p2_l), unsafe_allow_html=True)

                # 对比成交线索数卡片
                with col2:
                    st.markdown('''
                    <div class="metric-card compare">
                        <p class="card-title">{p2_name} 成交线索</p>
                        <p class="card-value">{p2_c:,}</p>
                    </div>
                    '''.format(p2_name=period2_name, p2_c=p2_c), unsafe_allow_html=True)

                # 对比成交率卡片
                with col3:
                    st.markdown('''
                    <div class="metric-card compare">
                        <p class="card-title">{p2_name} 成交率</p>
                        <p class="card-value">{p2_r:.1f}%</p>
                    </div>
                    '''.format(p2_name=period2_name, p2_r=p2_r), unsafe_allow_html=True)

                # 对比合同金额卡片
                with col4:
                    st.markdown('''
                    <div class="metric-card compare">
                        <p class="card-title">{p2_name} 合同金额</p>
                        <p class="card-value">¥{p2_a:,.1f}</p>
                    </div>
                    '''.format(p2_name=period2_name, p2_a=p2_a), unsafe_allow_html=True)
    with Col3:
        # 客户规模分析
        with st.container():
            # 处理缺失值并统计
            df_one["客户规模"] = df_one["客户规模"].fillna("未知")
            size_counts = df_one["客户规模"].value_counts().reset_index()
            size_counts.columns = ["客户规模", "数量"]
            # 计算百分比并格式化
            total = size_counts["数量"].sum()
            size_counts["百分比"] = (size_counts["数量"] / total * 100).apply(lambda x: f"{x:.1f}%")
            # 创建美观的表格
            st.dataframe(
                size_counts.style
                .set_table_styles([
                    {"selector": "th", "props": [("background-color", "#f0f2f6"),
                                                 ("font-weight", "bold"),
                                                 ("text-align", "center")]},
                    {"selector": "td", "props": [("text-align", "center"),
                                                 ("padding", "4px"),
                                                 ("vertical-align", "middle")]},
                    {"selector": "tr:nth-child(even)", "props": [("background-color", "#f9f9f9")]}
                ])
            )

    Col1, Col2, Col3, Col4 = st.columns(4)
    with Col1:
        # 客户来源分布
        with st.container():
            # 统计各地区企业数量
            region_counts = df_one["客户来源"].value_counts().reset_index()
            region_counts.columns = ["客户来源", "数量"]

            # 按预设顺序排序
            region_counts["客户来源"] = pd.Categorical(region_counts["客户来源"])
            region_counts = region_counts.sort_values("客户来源").dropna()

            custom_colors = [
                "#3498db", "#e74c3c", "#2ecc71", "#9b59b6", "#e67e22",  # 蓝、红、绿、紫、橙
                "#f1c40f", "#1abc9c", "#34495e", "#d35400", "#8e44ad"  # 黄、青、深蓝灰、深橙、深紫
            ]

            # 使用 Seaborn 绘制美观的横向条形图
            fig, ax = plt.subplots(figsize=(10, 8))  # 适当增加高度便于横向显示
            sns.barplot(
                x="数量",
                y="客户来源",  # 交换x和y轴
                data=region_counts,
                palette=custom_colors,
                ax=ax
            )

            # 添加数据标签（调整位置适应横向条形图）
            for p in ax.patches:
                ax.annotate(
                    f'{int(p.get_width())}',  # 使用p.get_width()获取数值
                    (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left',  # 标签居左
                    va='center',
                    fontsize=12,
                    color='black',
                    xytext=(10, 0),  # 向右偏移10像素
                    textcoords='offset points'
                )

            # 设置图表样式
            ax.set_title("客户来源分布", fontsize=16, pad=20)
            ax.set_xlabel("企业数量", fontsize=14, labelpad=10)
            ax.set_ylabel("客户来源", fontsize=14, labelpad=10)
            ax.tick_params(axis='both', which='major', labelsize=12)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='x', linestyle='--', alpha=0.7)  # 修改为x轴网格线

            # 显示图表
            st.pyplot(fig)
    with Col2:
        # 咨询产品分布
        with st.container():
            # 统计各地区企业数量
            region_counts = df_one["托管/咨询产品"].value_counts().reset_index()
            region_counts.columns = ["托管/咨询产品", "数量"]

            # 按预设顺序排序
            region_counts["托管/咨询产品"] = pd.Categorical(region_counts["托管/咨询产品"])
            region_counts = region_counts.sort_values("托管/咨询产品").dropna()

            custom_colors = [
                "#3498db", "#e74c3c", "#2ecc71", "#9b59b6",  # 蓝、红、绿、紫
                "#e67e22", "#f1c40f", "#1abc9c", "#34495e",  # 橙、黄、青、深蓝灰
                "#d35400", "#8e44ad", "#27ae60", "#f39c12",  # 深橙、深紫、深绿、金黄
                "#16a085", "#2980b9", "#8e44ad", "#c0392b",  # 深青、中蓝、深紫、暗红
            ]

            # 使用 Seaborn 绘制美观的横向条形图
            fig, ax = plt.subplots(figsize=(10, 8))  # 适当增加高度便于横向显示
            sns.barplot(
                x="数量",
                y="托管/咨询产品",  # 交换x和y轴
                data=region_counts,
                palette=custom_colors,
                ax=ax
            )

            # 添加数据标签（调整位置适应横向条形图）
            for p in ax.patches:
                ax.annotate(
                    f'{int(p.get_width())}',  # 使用p.get_width()获取数值
                    (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left',  # 标签居左
                    va='center',
                    fontsize=12,
                    color='black',
                    xytext=(10, 0),  # 向右偏移10像素
                    textcoords='offset points'
                )

            # 设置图表样式
            ax.set_title("托管/咨询产品分布", fontsize=16, pad=20)
            ax.set_xlabel("企业数量", fontsize=14, labelpad=10)
            ax.set_ylabel("托管/咨询产品", fontsize=14, labelpad=10)
            ax.tick_params(axis='both', which='major', labelsize=12)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='x', linestyle='--', alpha=0.7)  # 修改为x轴网格线

            # 显示图表
            st.pyplot(fig)
    with Col3:
        # 一级行业分布
        with st.container():
            # 统计各地区企业数量
            region_counts = df_one["一级行业"].value_counts().reset_index()
            region_counts.columns = ["一级行业", "数量"]

            # 按预设顺序排序
            region_counts["一级行业"] = pd.Categorical(region_counts["一级行业"])
            region_counts = region_counts.sort_values("一级行业").dropna()

            custom_colors = [
                "#3498db", "#e74c3c", "#2ecc71", "#9b59b6", "#e67e22",  # 蓝、红、绿、紫、橙
                "#f1c40f", "#1abc9c", "#34495e", "#d35400", "#8e44ad"  # 黄、青、深蓝灰、深橙、深紫
            ]

            # 使用 Seaborn 绘制美观的横向条形图
            fig, ax = plt.subplots(figsize=(10, 8))  # 适当增加高度便于横向显示
            sns.barplot(
                x="数量",
                y="一级行业",  # 交换x和y轴
                data=region_counts,
                palette=custom_colors,
                ax=ax
            )

            # 添加数据标签（调整位置适应横向条形图）
            for p in ax.patches:
                ax.annotate(
                    f'{int(p.get_width())}',  # 使用p.get_width()获取数值
                    (p.get_width(), p.get_y() + p.get_height() / 2),
                    ha='left',  # 标签居左
                    va='center',
                    fontsize=12,
                    color='black',
                    xytext=(10, 0),  # 向右偏移10像素
                    textcoords='offset points'
                )

            # 设置图表样式
            ax.set_title("一级行业分布", fontsize=16, pad=20)
            ax.set_xlabel("企业数量", fontsize=14, labelpad=10)
            ax.set_ylabel("一级行业", fontsize=14, labelpad=10)
            ax.tick_params(axis='both', which='major', labelsize=12)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.grid(axis='x', linestyle='--', alpha=0.7)  # 修改为x轴网格线

            # 显示图表
            st.pyplot(fig)
    with Col4:
        # 二级行业分布
        with st.container():
            # 获取所有唯一的一级行业
            unique_primary_industries = df_one["一级行业"].unique()
            unique_primary_industries = [industry for industry in unique_primary_industries if pd.notna(industry)]
            if not unique_primary_industries:
                st.warning("数据中没有找到一级行业信息")
                st.stop()
            # 创建一级行业下拉单选框
            selected_primary_industry = st.selectbox(
                "",
                ["全部"] + list(unique_primary_industries),
                label_visibility="collapsed"
            )
            # 根据选择的一级行业筛选数据
            if selected_primary_industry == "全部":
                filtered_df = df_one
            else:
                filtered_df = df_one[df_one["一级行业"] == selected_primary_industry]
            # 统计筛选后的二级行业数量
            if filtered_df.empty:
                st.info(f"暂无 '{selected_primary_industry}' 一级行业的二级行业数据")
            else:
                region_counts = filtered_df["二级行业"].value_counts().reset_index()
                region_counts.columns = ["二级行业", "数量"]

                # 按二级行业名称排序
                region_counts["二级行业"] = pd.Categorical(region_counts["二级行业"])
                region_counts = region_counts.sort_values("二级行业").dropna()

                custom_colors = [
                    "#3498db", "#e74c3c", "#2ecc71", "#9b59b6", "#e67e22",  # 蓝、红、绿、紫、橙
                    "#f1c40f", "#1abc9c", "#34495e", "#d35400", "#8e44ad"  # 黄、青、深蓝灰、深橙、深紫
                ]
                # 使用 Seaborn 绘制美观的横向条形图
                fig, ax = plt.subplots(figsize=(10, 8))  # 适当增加高度便于横向显示
                sns.barplot(
                    x="数量",
                    y="二级行业",  # 交换x和y轴
                    data=region_counts,
                    palette=custom_colors,
                    ax=ax
                )
                # 添加数据标签（调整位置适应横向条形图）
                for p in ax.patches:
                    ax.annotate(
                        f'{int(p.get_width())}',  # 使用p.get_width()获取数值
                        (p.get_width(), p.get_y() + p.get_height() / 2),
                        ha='left',  # 标签居左
                        va='center',
                        fontsize=12,
                        color='black',
                        xytext=(10, 0),  # 向右偏移10像素
                        textcoords='offset points'
                    )
                # 设置图表样式
                ax.set_xlabel("企业数量", fontsize=14, labelpad=10)
                ax.set_ylabel("二级行业", fontsize=14, labelpad=10)
                ax.tick_params(axis='both', which='major', labelsize=12)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.grid(axis='x', linestyle='--', alpha=0.7)  # 修改为x轴网格线

                # 显示图表
                st.pyplot(fig)

def dashboard_page_statistic():
    get_local_data()

# 新增：启动时自动检查记住的凭证
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = "匿名用户"
if 'current_page' not in st.session_state:
    st.session_state.current_page = None
if 'remember_me' not in st.session_state:
    st.session_state.remember_me = False


# 主程序逻辑
if not st.session_state['authenticated']:
    # 未登录状态显示登录页面
    login_page()
else:
    # 侧边栏导航
    with st.sidebar:
        # 退出登录 - 新增清除凭证
        if st.button(label="退出登录", type="secondary", help="点击退出当前账户", use_container_width=True):
            log_action("用户执行退出登录操作", "认证模块")
            st.session_state['authenticated'] = False
            delete_credentials()  # 退出时清除凭证
            st.rerun()
        pages = ["公有云", "市场部", "事业一部", "申请统计"]
        icons = ['bar-chart', 'building', 'gear', 'file-text']
        if st.session_state.get('role') == 'admin':
            pages.extend(["用户管理", "访问日志"])
            icons.extend(['person-plus', 'book'])

        page = option_menu(
            menu_title="主菜单",
            options=pages,
            icons=icons,
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

        # 记录页面跳转
        if st.session_state.current_page != page:
            log_action(f"用户切换页面至：{page}", "系统模块")
            st.session_state.current_page = page

    # 页面内容显示
    if page == "公有云":
        dashboard_page_saas()

    elif page == "用户管理":
        if st.session_state.get('role') == 'admin':
            user_management()
        else:
            st.error("你没有权限访问此页面", icon="❌")

    elif page == "访问日志":
        if st.session_state.get('role') == 'admin':
            log_viewer()
        else:
            st.error("你没有权限访问此页面", icon="❌")

    elif page == "市场部":
        dashboard_page_market()

    elif page == "事业一部":
        dashboard_page_one()

    elif page == "申请统计":
        dashboard_page_statistic()