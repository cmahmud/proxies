# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 379
- HTTP: 244 alive / 70 gold
- HTTPS: 186 alive / 22 gold
- SOCKS4: 226 alive / 140 gold
- SOCKS5: 220 alive / 147 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25268
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
