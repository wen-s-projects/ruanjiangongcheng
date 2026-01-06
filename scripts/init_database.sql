-- 初始化数据库脚本

-- 创建数据库（如果不存在）
CREATE DATABASE IF NOT EXISTS CalorieSystem DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE CalorieSystem;

-- 创建管理员表
CREATE TABLE IF NOT EXISTS Admin (
  admin_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='管理员表';

-- 创建用户表
CREATE TABLE IF NOT EXISTS User (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  photo VARCHAR(255) NULL,
  background VARCHAR(255) NULL,
  introduction TEXT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  is_staff BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户表';

-- 创建身体数据表
CREATE TABLE IF NOT EXISTS BodyData (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL UNIQUE,
  gender TINYINT NULL,
  age INT NOT NULL,
  height DECIMAL(5,1) NOT NULL,
  weight DECIMAL(5,1) NOT NULL,
  fat_rate DECIMAL(4,1) NOT NULL,
  bmi DECIMAL(4,1) NULL,
  basic_activity_level TINYINT NULL,
  basal_metabolic_rate DECIMAL(6,1) NULL,
  FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
  INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='身体数据表';

-- 创建饮食总表
CREATE TABLE IF NOT EXISTS Event (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  event_record VARCHAR(500) NOT NULL,
  event_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  remarks VARCHAR(200) NULL,
  FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
  INDEX idx_user_id (user_id),
  INDEX idx_event_time (event_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='饮食总表';

-- 创建食物字典表
CREATE TABLE IF NOT EXISTS FoodDict (
  id INT AUTO_INCREMENT PRIMARY KEY,
  food_name VARCHAR(50) NOT NULL UNIQUE,
  calorie DECIMAL(6,1) NOT NULL,
  INDEX idx_food_name (food_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='食物字典表';

-- 创建食物摄入记录表
CREATE TABLE IF NOT EXISTS FoodRecord (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  food_id INT NOT NULL,
  intake_time DATETIME DEFAULT CURRENT_TIMESTAMP,
  meal_type TINYINT NOT NULL,
  intake_amount DECIMAL(6,1) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE,
  FOREIGN KEY (food_id) REFERENCES FoodDict(id) ON DELETE CASCADE,
  INDEX idx_user_id (user_id),
  INDEX idx_intake_time (intake_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='食物摄入记录表';

-- 创建文章表
CREATE TABLE IF NOT EXISTS Article (
  id INT AUTO_INCREMENT PRIMARY KEY,
  author_id INT NOT NULL,
  title VARCHAR(200) NOT NULL,
  slug VARCHAR(200) NOT NULL UNIQUE,
  markdown TEXT NOT NULL,
  rendered_html TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'draft',
  allow_comments BOOLEAN DEFAULT TRUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (author_id) REFERENCES User(id) ON DELETE CASCADE,
  INDEX idx_author_id (author_id),
  INDEX idx_slug (slug),
  INDEX idx_status (status),
  INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='文章表';

-- 创建标签表
CREATE TABLE IF NOT EXISTS Tag (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL UNIQUE,
  slug VARCHAR(50) NOT NULL UNIQUE,
  count INT DEFAULT 0,
  INDEX idx_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='标签表';

-- 创建文章标签关联表
CREATE TABLE IF NOT EXISTS ArticleTag (
  id INT AUTO_INCREMENT PRIMARY KEY,
  article_id INT NOT NULL,
  tag_id INT NOT NULL,
  FOREIGN KEY (article_id) REFERENCES Article(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES Tag(id) ON DELETE CASCADE,
  UNIQUE KEY unique_article_tag (article_id, tag_id),
  INDEX idx_article_id (article_id),
  INDEX idx_tag_id (tag_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='文章标签关联表';

-- 创建评论表
CREATE TABLE IF NOT EXISTS Comment (
  id INT AUTO_INCREMENT PRIMARY KEY,
  article_id INT NOT NULL,
  author_id INT NULL,
  content TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'active',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (article_id) REFERENCES Article(id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES User(id) ON DELETE SET NULL,
  INDEX idx_article_id (article_id),
  INDEX idx_author_id (author_id),
  INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='评论表';

-- 创建文章图片表
CREATE TABLE IF NOT EXISTS ArticleImage (
  id INT AUTO_INCREMENT PRIMARY KEY,
  article_id INT NOT NULL,
  url VARCHAR(500) NOT NULL,
  thumb_url VARCHAR(500) NULL,
  width INT NULL,
  height INT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (article_id) REFERENCES Article(id) ON DELETE CASCADE,
  INDEX idx_article_id (article_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='文章图片表';

-- 创建文章食物引用表
CREATE TABLE IF NOT EXISTS ArticleFoodRef (
  id INT AUTO_INCREMENT PRIMARY KEY,
  article_id INT NOT NULL,
  food_id INT NULL,
  food_record_id INT NULL,
  note TEXT NULL,
  FOREIGN KEY (article_id) REFERENCES Article(id) ON DELETE CASCADE,
  FOREIGN KEY (food_id) REFERENCES FoodDict(id) ON DELETE SET NULL,
  FOREIGN KEY (food_record_id) REFERENCES FoodRecord(id) ON DELETE SET NULL,
  INDEX idx_article_id (article_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='文章食物引用表';

-- 插入示例数据
INSERT INTO FoodDict (food_name, calorie) VALUES
('米饭', 116),
('面条', 110),
('鸡蛋', 155),
('牛奶', 54),
('苹果', 52),
('香蕉', 89),
('鸡胸肉', 133),
('牛肉', 250),
('猪肉', 143),
('鱼', 106),
('蔬菜', 25),
('水果', 40);

INSERT INTO Admin (username, password) VALUES
('admin', '$2b$12$YourHashedPasswordHere');
