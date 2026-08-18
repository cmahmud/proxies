# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 278
- HTTP: 357 alive / 28 gold
- HTTPS: 153 alive / 5 gold
- SOCKS4: 229 alive / 133 gold
- SOCKS5: 217 alive / 112 gold

## Historical pool

- Discovered: 100083
- Ever alive: 12558
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
