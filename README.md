# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 382
- HTTP: 244 alive / 80 gold
- HTTPS: 167 alive / 21 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 244 alive / 140 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25285
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
