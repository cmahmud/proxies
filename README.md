# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 283
- HTTP: 294 alive / 36 gold
- HTTPS: 166 alive / 10 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 160 alive / 97 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13936
- Ever gold: 434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
