from itertools import groupby
import re

debug = 0

def isdirty(s):
   return True if re.search("[^A-Z]", s) else False

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

#  print("considering skus %r" % skus)
  if isdirty(skus):
      return -1

  #TODO: external flat file with simple format for update!
  freebies = {
      'E': [(2, 80, 'B')],
      'N': [(3, 120, 'M')],
      'R': [(3, 150, 'Q')]
  }
  #TODO: external flat file with simple format for update!
  offers = {
      'A': [(5, 200), (3, 130)],
      'B': [(2, 45)],
      'F': [(3, 20)],
      'H': [(10, 80), (5, 45)],
      'K': [(2, 150)],
      'P': [(5, 200)],
      'Q': [(3, 80)],
      'U': [(4, 120)],
      'V': [(3, 130), (2, 90)]
  }
  #TODO: external flat file with simple format for update!
  costs = {
     'A': 50,
     'B': 30,
     'C': 20,
     'D': 15,
     'E': 40,
     'F': 10,
     'G': 20,
     'H': 10,
     'I': 35,
     'J': 60,
     'K': 80,
     'L': 90,
     'M': 15,
     'N': 40,
     'O': 10,
     'P': 50,
     'Q': 30,
     'R': 50,
     'S': 30,
     'T': 20,
     'U': 40,
     'V': 50,
     'W': 20,
     'X': 90,
     'Y': 10,
     'Z': 50
  }
  a_skus = sorted(list(skus))

  # group and count
  counts = {}
  for k, g in groupby(a_skus):  # identity lambda as def
      counts[k] = len(list(g))

  # total
  val = 0

  # consider freebie offers
  for k, count in counts.items():
      if debug:
          print("considering %r, count %d" % (k, count))
      if k in freebies:
          for quantity, cost, free in freebies[k]:
              if debug:
                  print("considering freebie offer on %r, %d for %d" % (k, quantity, cost))
              while count >= quantity:
                  if debug:
                      print("offer requirements met, %d for %d on %r" % (quantity, cost, k))
                  val += cost
                  count -= quantity
                  counts[k] -= quantity  # outer context
                  free_items = list(free)
                  if len(free_items) > 0:
                      # reduce count(s) for given items
                      for p in free_items:
                          if p in counts:
                              counts[p] -= 1

  # consider value offers
  for k, count in counts.items():
      if debug:
          print("considering %r, count %d" % (k, count))
      if k in offers:
          # hmm, possible multiple offers.. order matters
          # TODO don't rely on order matters! sort by best deal value
          for quantity, cost in offers[k]:
              if debug:
                  print("considering offer on %r, %d for %d" % (k, quantity, cost))
              while count >= quantity:
                  if debug:
                     print("offer requirements met, %d for %d on %r" % (quantity, cost, k))
                  val += cost
                  count -= quantity
                  counts[k] -= quantity  # outer context

  # single item costs only remain
  for k, count in counts.items():
      val += (count * costs[k])

  if debug:
      print("returning %r for %r" % (val, skus))
  return val
