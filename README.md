# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 399
- HTTP: 301 alive / 90 gold
- HTTPS: 188 alive / 23 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 231 alive / 139 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29395
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
