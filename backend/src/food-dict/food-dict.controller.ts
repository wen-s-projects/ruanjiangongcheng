import * as express from 'express';
const router = express.Router();
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

// GET /api/food-dict - List all food items with pagination and search
router.get('/', async (req, res) => {
  try {
    const { page = 1, limit = 20, search } = req.query;
    const skip = (parseInt(page) - 1) * parseInt(limit);
    
    let whereClause: any = {};
    
    if (search) {
      whereClause = {
        foodName: {
          contains: search as string,
          mode: 'insensitive' // Case-insensitive search
        }
      };
    }
    
    const [foods, total] = await Promise.all([
      prisma.foodDict.findMany({
        where: whereClause,
        orderBy: {
          foodName: 'asc'
        },
        skip,
        take: parseInt(limit)
      }),
      prisma.foodDict.count({ where: whereClause })
    ]);
    
    res.json({
      foods,
      pagination: {
        page: parseInt(page),
        limit: parseInt(limit),
        total,
        totalPages: Math.ceil(total / parseInt(limit))
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Failed to get food items', details: error.message });
  }
});

// GET /api/food-dict/:id - Get food item by ID
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    const food = await prisma.foodDict.findUnique({
      where: { foodId: parseInt(id) }
    });
    
    if (!food) {
      return res.status(404).json({ error: 'Food item not found' });
    }
    
    res.json(food);
  } catch (error) {
    res.status(500).json({ error: 'Failed to get food item', details: error.message });
  }
});

// POST /api/food-dict - Create new food item
router.post('/', async (req, res) => {
  try {
    const { foodName, calorie } = req.body;
    
    if (!foodName || !calorie) {
      return res.status(400).json({ error: 'Food name and calorie are required' });
    }
    
    // Check if food already exists
    const existingFood = await prisma.foodDict.findUnique({ where: { foodName } });
    if (existingFood) {
      return res.status(409).json({ error: 'Food with this name already exists' });
    }
    
    const food = await prisma.foodDict.create({
      data: {
        foodName,
        calorie
      }
    });
    
    res.status(201).json(food);
  } catch (error) {
    res.status(500).json({ error: 'Failed to create food item', details: error.message });
  }
});

// PUT /api/food-dict/:id - Update food item
router.put('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { foodName, calorie } = req.body;
    
    // Check if food exists
    const existingFood = await prisma.foodDict.findUnique({ where: { foodId: parseInt(id) } });
    if (!existingFood) {
      return res.status(404).json({ error: 'Food item not found' });
    }
    
    // Check if new food name already exists (if changing name)
    if (foodName && foodName !== existingFood.foodName) {
      const duplicateFood = await prisma.foodDict.findUnique({ where: { foodName } });
      if (duplicateFood) {
        return res.status(409).json({ error: 'Food with this name already exists' });
      }
    }
    
    const updatedFood = await prisma.foodDict.update({
      where: { foodId: parseInt(id) },
      data: {
        foodName,
        calorie
      }
    });
    
    res.json(updatedFood);
  } catch (error) {
    res.status(500).json({ error: 'Failed to update food item', details: error.message });
  }
});

// DELETE /api/food-dict/:id - Delete food item
router.delete('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    // Check if food exists
    const existingFood = await prisma.foodDict.findUnique({ where: { foodId: parseInt(id) } });
    if (!existingFood) {
      return res.status(404).json({ error: 'Food item not found' });
    }
    
    await prisma.foodDict.delete({ where: { foodId: parseInt(id) } });
    res.status(204).send();
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete food item', details: error.message });
  }
});

module.exports = router;