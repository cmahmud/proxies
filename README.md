# SyndProxy private pool

## Current pool

- Alive now: 1535
- Gold now: 644
- HTTP: 523 alive / 214 gold
- HTTPS: 431 alive / 113 gold
- SOCKS4: 238 alive / 158 gold
- SOCKS5: 343 alive / 159 gold

## Historical pool

- Discovered: 141248
- Ever alive: 24127
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
