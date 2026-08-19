# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 518
- HTTP: 345 alive / 149 gold
- HTTPS: 228 alive / 89 gold
- SOCKS4: 219 alive / 148 gold
- SOCKS5: 202 alive / 132 gold

## Historical pool

- Discovered: 117160
- Ever alive: 17643
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
