# Expert System - Skin Diagnosis using Forward Chaining

## 📚 Project Overview

This project is a solution to the **Midterm Exam** for the **Expert System** subject. It implements a **forward chaining inference engine** to diagnose skin conditions based on symptoms and treatments using rule-based reasoning.

## 📋 Exam Question

### Problem Statement

Given the following knowledge base rules:

- **R1** → IF `Pembersih dengan Salicylic Acid` AND `Spot Treatment dengan Benzoyl Peroxide` THEN `Jerawat`
- **R2** → IF `Flek Hitam` AND `Bintik Putih` THEN `Pigmentasi Karena Hormon`
- **R3** → IF `Pembersih dengan Salicylic Acid` AND `Spot Treatment dengan Benzoyl Peroxide` THEN `Bekas Jerawat`
- **R4** → IF `Pori-pori Besar` AND `Kulit Kusam` AND `Kulit Reda` THEN `Kulit Terkontaminasi Debu`
- **R5** → IF `Pembersih dengan Salicylic Acid` AND `Spot Treatment` THEN `Kulit Terbakar Matahari`

**Given Facts:**
- Kulit Kusam
- Gatal-gatal
- Pori-pori Besar

**Task:** Determine the diagnosis using **forward chaining** method and create the decision tree.

## 🎯 Solution

### Answer

Based on the forward chaining analysis with the given facts:

**Initial Facts:**
```
- Kulit Kusam
- Gatal-gatal
- Pori-pori Besar
```

**Forward Chaining Process:**

The system evaluates all rules against the working memory:

1. **Iteration 1:**
   - Working Memory: {Kulit Kusam, Gatal-gatal, Pori-pori Besar}
   - Checking all rules...
   - ❌ **R1**: Requires "Pembersih dengan Salicylic Acid" AND "Spot Treatment dengan Benzoyl Peroxide" - NOT SATISFIED
   - ❌ **R2**: Requires "Flek Hitam" AND "Bintik Putih" - NOT SATISFIED
   - ❌ **R3**: Requires "Pembersih dengan Salicylic Acid" AND "Spot Treatment dengan Benzoyl Peroxide" - NOT SATISFIED
   - ❌ **R4**: Requires "Pori-pori Besar" AND "Kulit Kusam" AND "Kulit Reda" - PARTIALLY SATISFIED (missing "Kulit Reda")
   - ❌ **R5**: Requires "Pembersih dengan Salicylic Acid" AND "Spot Treatment" - NOT SATISFIED

**Result:** ❌ **No rules can be fired**

### Conclusion

**No diagnosis can be determined** because none of the rules have all their conditions satisfied by the given facts. The system cannot infer any skin condition diagnosis.

**Reason:**
- The given facts (Kulit Kusam, Gatal-gatal, Pori-pori Besar) do not completely match any rule's antecedent conditions
- R4 comes closest but still requires "Kulit Reda" to be triggered
- The fact "Gatal-gatal" is not part of any rule's conditions

### Decision Tree

```
Initial Facts:
  ├─ Gatal-gatal
  ├─ Kulit Kusam
  └─ Pori-pori Besar
      |
      ├─ Check R1: ❌ (Missing: Pembersih dengan Salicylic Acid, Spot Treatment dengan Benzoyl Peroxide)
      ├─ Check R2: ❌ (Missing: Flek Hitam, Bintik Putih)
      ├─ Check R3: ❌ (Missing: Pembersih dengan Salicylic Acid, Spot Treatment dengan Benzoyl Peroxide)
      ├─ Check R4: ❌ (Missing: Kulit Reda)
      └─ Check R5: ❌ (Missing: Pembersih dengan Salicylic Acid, Spot Treatment)
      
Final Result: NO DIAGNOSIS
```

## 🚀 Features

The implementation includes:

1. **Knowledge Base Management**
   - Stores rules with conditions, conclusions, and metadata
   - Confidence levels for each diagnosis
   - Explanations and recommendations

2. **Forward Chaining Inference Engine**
   - Iterative rule matching
   - Working memory management
   - Conflict resolution
   - Detailed execution trace

3. **Decision Tree Visualization**
   - Visual representation of inference process
   - Shows which rules fired and in what order

4. **Interactive Mode**
   - User-friendly symptom selection
   - Real-time diagnosis
   - Detailed explanations

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone or download the repository:
```bash
git clone https://github.com/handikatriarlan/expert-system-midterm-exam.git
cd expert-system-midterm-exam
```

2. No additional dependencies required (uses only Python standard library)

## 📖 Usage

### Running the Program

```bash
python diagnosis_forward_chaining.py
```

### Demo Mode (Exam Case)

The program automatically runs with the exam question's facts:
```python
facts = {"Kulit Kusam", "Gatal-gatal", "Pori-pori Besar"}
```

### Interactive Mode

After the demo, you can try other cases:

1. Choose symptoms by number (comma-separated)
2. Type `default` to use the exam case again
3. Get instant diagnosis with explanations

### Example Output

```
============================================================
SISTEM PAKAR DIAGNOSIS KULIT
Forward Chaining Method
============================================================

FAKTA AWAL (3 fakta):
  1. Gatal-gatal
  2. Kulit Kusam
  3. Pori-pori Besar

============================================================
ITERASI 1
============================================================
Working Memory: ['Gatal-gatal', 'Kulit Kusam', 'Pori-pori Besar']

============================================================
HASIL DIAGNOSIS
============================================================

❌ Tidak ada aturan yang terpenuhi.
Tidak dapat menentukan diagnosis berdasarkan fakta yang diberikan.

Saran: Tambahkan gejala atau perawatan yang sedang digunakan.
```

## 🧪 Testing Different Cases

Try these test cases to see the system in action:

### Case 1: Acne Diagnosis
```python
facts = {
    "Pembersih dengan Salicylic Acid", 
    "Spot Treatment dengan Benzoyl Peroxide"
}
# Expected: Jerawat, Bekas Jerawat
```

### Case 2: Pigmentation
```python
facts = {
    "Flek Hitam", 
    "Bintik Putih"
}
# Expected: Pigmentasi Karena Hormon
```

### Case 3: Dust Contamination
```python
facts = {
    "Pori-pori Besar", 
    "Kulit Kusam", 
    "Kulit Reda"
}
# Expected: Kulit Terkontaminasi Debu
```

## 📊 System Architecture

```
┌─────────────────────────────────────────┐
│         Expert System                    │
│                                          │
│  ┌────────────────┐  ┌───────────────┐ │
│  │ Knowledge Base │  │   Inference   │ │
│  │                │  │     Engine    │ │
│  │  - Rules (R1-R5)│──▶│   (Forward   │ │
│  │  - Facts       │  │   Chaining)   │ │
│  │  - Symptoms    │  │               │ │
│  └────────────────┘  └───────┬───────┘ │
│                              │          │
│                              ▼          │
│                      ┌───────────────┐  │
│                      │   Diagnosis   │  │
│                      │   + Tree      │  │
│                      └───────────────┘  │
└─────────────────────────────────────────┘
```

## 🧠 Forward Chaining Algorithm

```python
1. Initialize working_memory with initial facts
2. REPEAT:
   3. FOR each rule in knowledge_base:
      4. IF rule.conditions ⊆ working_memory AND rule not fired:
         5. Add rule.conclusion to working_memory
         6. Mark rule as fired
         7. Set changed = TRUE
   8. UNTIL changed = FALSE
9. Return final working_memory and fired rules
```

## 📝 Code Structure

```
diagnosis_forward_chaining.py
├── KnowledgeBase         # Stores rules and available symptoms
├── InferenceEngine       # Implements forward chaining logic
│   ├── forward_chaining()      # Main inference method
│   └── generate_decision_tree() # Creates decision tree visualization
└── ExpertSystem          # Main system controller
    ├── run_with_facts()  # Run diagnosis with given facts
    └── interactive_mode() # User interaction mode
```

## 🎓 Learning Objectives

This project demonstrates understanding of:

1. **Forward Chaining Inference**
   - Data-driven reasoning
   - Pattern matching
   - Working memory management

2. **Expert Systems Components**
   - Knowledge base representation
   - Inference engine design
   - User interface

3. **Rule-Based Systems**
   - IF-THEN rules
   - Fact base
   - Conflict resolution

## 🔍 Key Insights from the Exam Question

The exam question tests understanding that:

1. **Forward chaining requires complete rule satisfaction** - All conditions must be present in working memory
2. **Irrelevant facts don't trigger rules** - "Gatal-gatal" exists but isn't used by any rule
3. **Partial matching is insufficient** - R4 almost matches but missing one condition
4. **The system can conclude with no diagnosis** - A valid outcome when no rules fire

## 👨‍💻 Author

**Arlan Tri Handika**

- Course: Expert System
- Exam: Midterm Exam
- Date: 2025

---

**Note:** This implementation goes beyond the basic exam requirements by adding:
- Confidence scores
- Detailed explanations
- Treatment recommendations
- Interactive mode
- Comprehensive tracing

The core answer to the exam question is: **No diagnosis can be determined** from the given facts using the provided rules.
