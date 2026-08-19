# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 407
- HTTP: 399 alive / 92 gold
- HTTPS: 260 alive / 16 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 308 alive / 151 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21212
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
