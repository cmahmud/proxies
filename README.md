# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 489
- HTTP: 375 alive / 129 gold
- HTTPS: 239 alive / 86 gold
- SOCKS4: 196 alive / 121 gold
- SOCKS5: 233 alive / 153 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17840
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
