# main.py - 使用同一个端口的完整解决方案
from flask import Flask, render_template, request, jsonify
import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

# 导入算法模块
from alg1_app import Algorithm1
from alg2_app import Algorithm2

# 创建算法实例
alg1 = Algorithm1()
alg2 = Algorithm2()


# 首页 - 导航页
@app.route('/')
def index():
    return render_template('nav.html')


# 算法一页面
@app.route('/alg1')
def alg1_page():
    return render_template('alg1.html')


# 算法一API - 正变换
@app.route('/api/alg1/forward', methods=['POST'])
def alg1_forward():
    data = request.json
    n = data.get('n', 0)
    try:
        result = alg1.forward_transform(n)
        return jsonify({
            'success': True,
            'result': result,
            'message': f'✅ 正变换完成\n输入: {n}\n输出: {result}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'result': 0,
            'message': f'❌ 错误: {str(e)}'
        })


# 算法一API - 逆变换
@app.route('/api/alg1/inverse', methods=['POST'])
def alg1_inverse():
    data = request.json
    n = data.get('n', 0)
    try:
        result = alg1.inverse_transform(n)
        return jsonify({
            'success': True,
            'result': result,
            'message': f'✅ 逆变换完成\n输入: {n}\n输出: {result}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'result': 0,
            'message': f'❌ 错误: {str(e)}'
        })


# 算法二页面
@app.route('/alg2')
def alg2_page():
    return render_template('alg2.html')


# 算法二API - 正变换
@app.route('/api/alg2/encode', methods=['POST'])
def alg2_encode():
    data = request.json
    n = data.get('n', 0)
    try:
        result = alg2.encode_transform(n)
        return jsonify({
            'success': True,
            'result': result,
            'message': f'✅ 正变换完成\n输入: {n}\n输出: {result}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'result': 0,
            'message': f'❌ 错误: {str(e)}'
        })


# 算法二API - 逆变换
@app.route('/api/alg2/decode', methods=['POST'])
def alg2_decode():
    data = request.json
    n = data.get('n', 0)
    try:
        result = alg2.decode_transform(n)
        return jsonify({
            'success': True,
            'result': result,
            'message': f'✅ 逆变换完成\n输入: {n}\n输出: {result}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'result': 0,
            'message': f'❌ 错误: {str(e)}'
        })


# 健康检查
@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': '数字变换系统'})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
