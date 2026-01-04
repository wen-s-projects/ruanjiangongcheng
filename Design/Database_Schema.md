1.数据库建设
Admin
- AdminName          （主键，建议自增，如INT类型）
- AdminPassword    （非空，唯一，避免重复用户名）

User（用户信息表）
- ID          （主键，建议自增，如INT类型）
- Username    （非空，唯一，避免重复用户名）
- Passport    （备注：存储用户登录凭证（加密后存储，如密码哈希值），修正命名首字母大写保持一致性）
- Photo       （存储用户头像路径/URL，允许为空）
- Background  （存储用户背景图路径/URL，允许为空）
- Introduction（用户个人简介，文本类型，允许为空）

BodyData（用户身体数据表）
- BodyID      （主键，建议自增）
- UserID      （外键，关联User表的ID，非空，确保绑定对应用户）
- Gender      （性别，如字符型/数字型，备注：男/女/未知）
- Age         （年龄，约束：BETWEEN 1 AND 100，修正原始合理范围的表述）
- Height      （身高，单位：厘米，约束：BETWEEN 30.0 AND 250.0 ，保留字段名）
- Weight      （体重，单位：千克，约束：BETWEEN 5.0 AND 300.0，保留原始范围）
- FatRate      （体脂率，约束：BETWEEN 0.0 AND 100.0，明确百分比范围）
- BMI         （身体质量指数，可实时计算也可存储，备注：BMI=体重(kg)/身高(m)²）
- BasicActivityLevel  （基础活动量，备注：对应活动系数分类（如1-久坐、2-轻度等））
- BasalMetabolicRate    （基础代谢，单位：大卡(kcal)，为基础代谢率计算值）

Event（用户饮食总表）
- EventID     （主键，建议自增）
- UserID      （外键，关联User表的ID，非空，绑定对应用户）
- EventRecord （饮食总记录内容，备注：如当日饮食总热量/饮食总结等，匹配“饮食总表”用途）
- EventTime   （记录时间，非空，建议默认当前时间，便于追溯）
- Remarks     （饮食备注，如“当日饮食偏油腻”等，允许为空）

FoodDict（食物热量基础字典表）
- FoodID      （主键，建议自增）
- FoodName    （食物名称，非空，唯一，避免重复录入同一种食物）
- Calorie     （热量，备注：单位：大卡(kcal)/100克，明确热量统计标准）

FoodRecord（用户食物摄入记录表（当日））
- RecordID  INT PRIMARY KEY AUTO_INCREMENT  -- 主键，自增，唯一标识每一条食物摄入记录
- UserID （关联User表的主键（ID），绑定对应用户）
- FoodID （外键，关联FoodDict表的主键（FoodID），绑定对应食物）
- IntakeTime （摄入时间，默认当前时间，便于筛选当日数据）
- MealType      （餐次类型：1-早餐/2-午餐/3-晚餐/4-加餐' ）
- IntakeAmount  （摄入量，单位：克（g））

2.数据库代码
CREATE DATABASE IF NOT EXISTS HealthSystem 
DEFAULT CHARSET=utf8mb4 
DEFAULT COLLATE utf8mb4_general_ci;

USE HealthSystem;

-- ----------------------------
-- 管理员表（Admin）
-- ----------------------------
CREATE TABLE Admin (
  AdminID INT PRIMARY KEY AUTO_INCREMENT COMMENT '管理员主键，自增唯一标识',
  Username VARCHAR(50) NOT NULL UNIQUE COMMENT '管理员用户名，非空且不可重复',
  Passport VARCHAR(255) NOT NULL COMMENT '登录凭证（加密后的密码哈希值）'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='管理员表';

-- ----------------------------
-- 用户信息表（User）
-- ----------------------------
CREATE TABLE User (
  ID INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户主键，自增唯一标识',
  Username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户用户名，非空且不可重复',
  Passport VARCHAR(255) NOT NULL COMMENT '登录凭证（加密后的密码哈希值）',
  Photo VARCHAR(255) NULL COMMENT '用户头像路径/URL，允许为空',
  Background VARCHAR(255) NULL COMMENT '用户背景图路径/URL，允许为空',
  Introduction TEXT NULL COMMENT '用户个人简介，文本类型，允许为空'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表';

-- ----------------------------
-- 用户身体数据表（BodyData）
-- （移除字段级CHECK约束，改为业务层校验）
-- ----------------------------
CREATE TABLE BodyData (
  BodyID INT PRIMARY KEY AUTO_INCREMENT COMMENT '身体数据主键，自增唯一标识',
  UserID INT NOT NULL COMMENT '外键，关联User表的ID',
  Gender TINYINT NULL COMMENT '性别：1-男/2-女/0-未知',
  Age TINYINT NOT NULL COMMENT '年龄，范围1-100岁',
  Height DECIMAL(5,1) NOT NULL COMMENT '身高（厘米），范围30.0-250.0cm',
  Weight DECIMAL(5,1) NOT NULL COMMENT '体重（千克），范围5.0-300.0kg',
  FatRate DECIMAL(4,1) NOT NULL COMMENT '体脂率（%），范围0.0-100.0%',
  BMI DECIMAL(4,1) NULL COMMENT '身体质量指数，计算公式：BMI=体重(kg)/身高(m)²',
  BasicActivityLevel TINYINT NULL COMMENT '基础活动量：1-久坐/2-轻度/3-中度/4-高度/5-极高',
  BasalMetabolicRate DECIMAL(6,1) NULL COMMENT '基础代谢率，单位：大卡(kcal)',
  FOREIGN KEY (UserID) REFERENCES User(ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户身体数据表';

-- ----------------------------
-- 用户饮食总表（Event）
-- ----------------------------
CREATE TABLE Event (
  EventID INT PRIMARY KEY AUTO_INCREMENT COMMENT '饮食总记录主键，自增唯一标识',
  UserID INT NOT NULL COMMENT '外键，关联User表的ID',
  EventRecord VARCHAR(500) NOT NULL COMMENT '饮食总记录内容（如当日饮食总热量/饮食总结）',
  EventTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录时间，默认当前时间',
  Remarks VARCHAR(200) NULL COMMENT '饮食备注，如“当日饮食偏油腻”',
  FOREIGN KEY (UserID) REFERENCES User(ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户饮食总表';

-- ----------------------------
-- 食物热量基础字典表（FoodDict）
-- ----------------------------
CREATE TABLE FoodDict (
  FoodID INT PRIMARY KEY AUTO_INCREMENT COMMENT '食物主键，自增唯一标识',
  FoodName VARCHAR(50) NOT NULL UNIQUE COMMENT '食物名称，非空且不可重复',
  Calorie DECIMAL(6,1) NOT NULL COMMENT '热量，单位：大卡(kcal)/100克'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='食物热量基础字典表';

-- ----------------------------
-- 用户食物摄入记录表（当日）（FoodRecord）
-- ----------------------------
CREATE TABLE FoodRecord (
  RecordID INT PRIMARY KEY AUTO_INCREMENT COMMENT '食物摄入记录主键，自增唯一标识',
  UserID INT NOT NULL COMMENT '外键，关联User表的主键ID',
  FoodID INT NOT NULL COMMENT '外键，关联FoodDict表的主键FoodID',
  IntakeTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '摄入时间，默认当前时间，便于筛选当日数据',
  MealType TINYINT NOT NULL COMMENT '餐次类型：1-早餐/2-午餐/3-晚餐/4-加餐',
  IntakeAmount DECIMAL(6,1) NOT NULL COMMENT '摄入量，单位：克（g）',
  FOREIGN KEY (UserID) REFERENCES User(ID),
  FOREIGN KEY (FoodID) REFERENCES FoodDict(FoodID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户食物摄入记录表（当日）';