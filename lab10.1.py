import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class FirmTree:
    def __init__(self):
        self.root = None
        self.queue = []  # черга для level-order вставки

    def insert(self, name):
        new_node = Node(name)

        if not self.root:
            self.root = new_node
            self.queue.append(new_node)
            return

        # Пошук місця через чергу
        while True:
            node = self.queue[0]

            if node.left is None:
                node.left = new_node
                break
            elif node.right is None:
                node.right = new_node
                break
            else:
                self.queue.pop(0)

        self.queue.append(new_node)

    # Пошук
    def search(self, node, target):
        if node is None:
            return None
        if node.name == target:
            return node
        return self.search(node.left, target) or self.search(node.right, target)

    def delete(self, target):
        if not self.root:
            return False

        # Level-order обхід
        queue = [self.root]
        node_to_delete = None
        last_node = None
        parent_of_last = None

        while queue:
            current = queue.pop(0)
            if current.name == target:
                node_to_delete = current
            if current.left:
                parent_of_last = current
                last_node = current.left
                queue.append(current.left)
            if current.right:
                parent_of_last = current
                last_node = current.right
                queue.append(current.right)

        if node_to_delete and last_node:
            node_to_delete.name = last_node.name  # заміна
            # видаляємо останній
            if parent_of_last.right == last_node:
                parent_of_last.right = None
            else:
                parent_of_last.left = None
            return True

        return False

    # Обходи дерева
    def preorder(self, node, result):
        if node:
            result.append(node.name)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.name)
            self.inorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.name)

    def levelorder(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.name)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


tree = FirmTree()


def add_item():
    name = entry.get().strip()
    if name:
        tree.insert(name)
        messagebox.showinfo("Успіх", f"Елемент '{name}' додано!")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Помилка", "Введіть назву!")


def delete_item():
    target = entry.get().strip()
    if tree.delete(target):
        messagebox.showinfo("Успіх", f"Елемент '{target}' видалено.")
    else:
        messagebox.showerror("Помилка", f"Елемент '{target}' не знайдено.")
    entry.delete(0, tk.END)


def search_item():
    target = entry.get().strip()
    node = tree.search(tree.root, target)
    if node:
        messagebox.showinfo("Знайдено", f"Елемент '{target}' присутній у дереві.")
    else:
        messagebox.showerror("Немає", f"Елемент '{target}' не знайдено.")
    entry.delete(0, tk.END)


def show_preorder():
    res = []
    tree.preorder(tree.root, res)
    messagebox.showinfo("Preorder", " → ".join(res) if res else "Дерево пусте")


def show_inorder():
    res = []
    tree.inorder(tree.root, res)
    messagebox.showinfo("Inorder", " → ".join(res) if res else "Дерево пусте")


def show_postorder():
    res = []
    tree.postorder(tree.root, res)
    messagebox.showinfo("Postorder", " → ".join(res) if res else "Дерево пусте")


def show_levelorder():
    res = tree.levelorder()
    messagebox.showinfo("Level-order", " → ".join(res) if res else "Дерево пусте")


window = tk.Tk()
window.title("Структура фірми – Бінарне дерево")
window.geometry("500x350")

label = tk.Label(window, text="Введіть назву відділу / елемент дерева:")
label.pack(pady=5)

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

# Кнопки операцій
tk.Button(window, text="Додати елемент", width=20, command=add_item).pack(pady=5)
tk.Button(window, text="Видалити елемент", width=20, command=delete_item).pack(pady=5)
tk.Button(window, text="Пошук", width=20, command=search_item).pack(pady=5)

tk.Label(window, text="Обходи дерева:").pack(pady=10)

tk.Button(window, text="Preorder", width=15, command=show_preorder).pack()
tk.Button(window, text="Inorder", width=15, command=show_inorder).pack()
tk.Button(window, text="Postorder", width=15, command=show_postorder).pack()
tk.Button(window, text="Level-order", width=15, command=show_levelorder).pack()

window.mainloop()
