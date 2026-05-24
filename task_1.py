class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def print_list(self):
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(res))

    # 1. Реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Сортування вставками
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            
            # Вставка current у відсортовану частину
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
                
            current = next_node
            
        self.head = sorted_head

# 3. Об'єднання двох відсортованих списків
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy
    
    l1 = list1.head
    l2 = list2.head
    
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
        
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# --- Тестування Завдання 1 ---
if __name__ == "__main__":
    ll = LinkedList()
    for val in [3, 1, 4, 2]: ll.insert_at_end(val)
    
    print("Оригінальний список:")
    ll.print_list()
    
    ll.reverse()
    print("Реверсований список:")
    ll.print_list()
    
    ll.insertion_sort()
    print("Відсортований список:")
    ll.print_list()
    
    ll2 = LinkedList()
    for val in [0, 5, 6]: ll2.insert_at_end(val)
    
    print("Другий відсортований список:")
    ll2.print_list()
    
    merged = merge_sorted_lists(ll, ll2)
    print("Об'єднаний список:")
    merged.print_list()
