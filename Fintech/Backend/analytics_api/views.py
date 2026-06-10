from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection


def company_scores(request):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                symbol,
                health_score,
                health_label
            FROM fact_ml_scores
            ORDER BY health_score DESC
            LIMIT 20
        """)

        rows = cursor.fetchall()

    data = []

    for row in rows:

        data.append({
            "symbol": row[0],
            "health_score": float(row[1]) if row[1] else 0,
            "health_label": row[2]
        })

    return JsonResponse(data, safe=False)


def dashboard(request):

    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT
                symbol,
                health_score,
                health_label
            FROM fact_ml_scores
            ORDER BY health_score DESC
            LIMIT 20
        """)

        rows = cursor.fetchall()

    companies = []

    for row in rows:

        companies.append({
            "symbol": row[0],
            "score": float(row[1]) if row[1] else 0,
            "label": row[2]
        })

    return render(
        request,
        "dashboard.html",
        {"companies": companies}
    )


def company_detail(request, symbol):

    with connection.cursor() as cursor:

        # Company details
        cursor.execute(
            """
            SELECT
                c.company_name,
                m.health_score,
                m.health_label
            FROM dim_company c
            JOIN fact_ml_scores m
            ON c.symbol = m.symbol
            WHERE c.symbol = %s
            """,
            [symbol]
        )

        row = cursor.fetchone()

        if row is None:

            return JsonResponse({
                "error": f"Company '{symbol}' not found"
            })

        # Profit trend data
        cursor.execute(
            """
            SELECT
                year,
                sales,
                net_profit
            FROM fact_profit_loss
            WHERE symbol = %s
            ORDER BY year
            """,
    [symbol]
)

        financial_rows = cursor.fetchall()
        print(financial_rows)

    years = []
    sales = []
    profits = []

    for item in financial_rows:

        years.append(str(item[0]))
        sales.append(float(item[1]) if item[1] else 0)
        profits.append(float(item[2]) if item[2] else 0)

    company = {
        "symbol": symbol,
        "company_name": row[0],
        "health_score": float(row[1]) if row[1] else 0,
        "health_label": row[2]
    }

    print(years)
    print(sales)
    print(profits)
    context = {
        "company": company,
        "years": years,
        "sales": sales,
        "profits": profits
    }

    return render(
        request,
        "company_detail.html",
        context
    )
def top_companies(request):

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                c.company_name,
                c.symbol,
                m.health_score,
                m.health_label
            FROM dim_company c
            JOIN fact_ml_scores m
            ON c.symbol = m.symbol
            ORDER BY m.health_score DESC
            LIMIT 20
            """
        )

        rows = cursor.fetchall()

    companies = []

    for row in rows:

        companies.append({
            "company_name": row[0],
            "symbol": row[1],
            "health_score": row[2],
            "health_label": row[3]
        })

    return render(
        request,
        "top_companies.html",
        {"companies": companies}
    )

def search_company(request):

    query = request.GET.get("query", "")

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                company_name,
                symbol
            FROM dim_company
            WHERE symbol ILIKE %s
            OR company_name ILIKE %s
            LIMIT 20
            """,
            [f"%{query}%", f"%{query}%"]
        )

        rows = cursor.fetchall()

    companies = []

    for row in rows:

        companies.append({
            "company_name": row[0],
            "symbol": row[1]
        })

    return render(
        request,
        "search_results.html",
        {
            "companies": companies,
            "query": query
        }
    )