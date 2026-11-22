# === Stage 9: Поиск по нескольким словам ===
# Project: PotteryLog
def search_products(products, terms):
    if not terms:
        return list(products)
    
    normalized = []
    for term in terms:
        stripped = term.strip()
        if not stripped:
            continue
        if stripped.startswith('-'):
            normalized.append(('exclude', stripped[1:].strip()))
        else:
            normalized.append(('include', stripped))
    
    if not normalized:
        return list(products)
    
    include_terms = [t[1] for t in normalized if t[0] == 'include']
    exclude_terms = [t[1] for t in normalized if t[0] == 'exclude']
    
    if include_terms:
        include_patterns = [
            re.compile(term, re.IGNORECASE) for term in include_terms
        ]
        include_result = [
            product for product in products
            if any(pattern.search(product.name) for pattern in include_patterns)
        ]
    else:
        include_result = list(products)
    
    if exclude_terms:
        exclude_patterns = [
            re.compile(term, re.IGNORECASE) for term in exclude_terms
        ]
        exclude_result = [
            product for product in include_result
            if not any(pattern.search(product.name) for pattern in exclude_patterns)
        ]
    else:
        exclude_result = include_result
    
    return exclude_result


def parse_search_query(query):
    if not query:
        return []
    return [token.strip() for token in query.split() if token.strip()]


def find_products(products, query):
    terms = parse_search_query(query)
    return search_products(products, terms)


if __name__ == '__main__':
    sample = [
        {'name': 'Кувшин', 'clay': 'глина', 'weight': 500, 'status': 'готов'},
        {'name': 'Чаша', 'clay': 'каолин', 'weight': 200, 'status': 'обожжена'},
        {'name': 'Ваза', 'clay': 'глина', 'weight': 800, 'status': 'готов'},
        {'name': 'Тарелка', 'clay': 'каолин', 'weight': 150, 'status': 'сырой'},
        {'name': 'Миска', 'clay': 'каолин', 'weight': 300, 'status': 'готов'},
    ]
    for query in ['кувшин', 'глина', 'глина -чаша', 'каолин -сырой']:
        print(f'Запрос: "{query}"')
        for product in find_products(sample, query):
            print(f'  - {product["name"]} ({product["clay"]}, {product["weight"]} г, {product["status"]})')
        print()
