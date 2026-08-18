# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 281
- HTTP: 315 alive / 29 gold
- HTTPS: 227 alive / 6 gold
- SOCKS4: 230 alive / 125 gold
- SOCKS5: 223 alive / 121 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13195
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
