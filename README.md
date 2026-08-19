# SyndProxy private pool

## Current pool

- Alive now: 1183
- Gold now: 406
- HTTP: 370 alive / 94 gold
- HTTPS: 252 alive / 15 gold
- SOCKS4: 234 alive / 149 gold
- SOCKS5: 327 alive / 148 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21196
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
