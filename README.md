# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 388
- HTTP: 247 alive / 80 gold
- HTTPS: 159 alive / 30 gold
- SOCKS4: 209 alive / 148 gold
- SOCKS5: 212 alive / 130 gold

## Historical pool

- Discovered: 163331
- Ever alive: 31858
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
