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
                "admin": {
                    "password": "admin123.",
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
                st.write("如有疑问，请联系管理员！！！")

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
    get_local_data()  # 上传数据

def dashboard_page_statistic():
    get_local_data()

# 启动时自动检查记住的凭证
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