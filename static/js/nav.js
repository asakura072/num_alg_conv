// static/js/nav.js - 简化的导航页面JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('导航页面加载完成');
    
    // 为卡片添加悬停效果
    const cards = document.querySelectorAll('.app-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // 处理按钮点击
    document.querySelectorAll('.card-button').forEach(button => {
        button.addEventListener('click', function(e) {
            // 显示加载动画
            const loadingOverlay = document.getElementById('loading');
            loadingOverlay.style.display = 'flex';
            
            // 添加淡入效果
            setTimeout(() => {
                loadingOverlay.style.opacity = '1';
            }, 10);
            
            // 如果页面跳转太慢，3秒后隐藏加载动画
            setTimeout(() => {
                loadingOverlay.style.opacity = '0';
                setTimeout(() => {
                    loadingOverlay.style.display = 'none';
                }, 300);
            }, 3000);
        });
    });
    
    // 添加键盘快捷键
    document.addEventListener('keydown', function(e) {
        // Alt+1 进入算法一
        if (e.altKey && e.key === '1') {
            e.preventDefault();
            document.getElementById('alg1-btn').click();
        }
        
        // Alt+2 进入算法二
        if (e.altKey && e.key === '2') {
            e.preventDefault();
            document.getElementById('alg2-btn').click();
        }
    });
    
    // 添加页面进入动画
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});