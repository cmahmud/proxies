# SyndProxy private pool

## Current pool

- Alive now: 661
- Gold now: 250
- HTTP: 219 alive / 28 gold
- HTTPS: 85 alive / 10 gold
- SOCKS4: 180 alive / 126 gold
- SOCKS5: 177 alive / 86 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9760
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
