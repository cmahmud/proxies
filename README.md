# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 245
- HTTP: 398 alive / 27 gold
- HTTPS: 193 alive / 1 gold
- SOCKS4: 205 alive / 122 gold
- SOCKS5: 224 alive / 95 gold

## Historical pool

- Discovered: 95391
- Ever alive: 10589
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
