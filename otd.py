#!/usr/bin/env python3
"""Compute an out-the-door price: item price + shipping + fees + sales tax."""
import argparse


def otd(price: float, tax_rate: float, shipping: float = 0.0, fees: float = 0.0, tax_shipping: bool = False) -> float:
    taxable = price + (shipping if tax_shipping else 0.0)
    return round(price + shipping + fees + taxable * tax_rate, 2)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("price", type=float)
    p.add_argument("--tax", type=float, default=0.0775, help="tax rate, e.g. 0.0775")
    p.add_argument("--shipping", type=float, default=0.0)
    p.add_argument("--fees", type=float, default=0.0)
    p.add_argument("--tax-shipping", action="store_true")
    a = p.parse_args()
    print(f"${otd(a.price, a.tax, a.shipping, a.fees, a.tax_shipping):.2f}")


if __name__ == "__main__":
    main()
