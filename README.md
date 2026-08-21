# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 402
- HTTP: 285 alive / 94 gold
- HTTPS: 176 alive / 20 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 235 alive / 138 gold

## Historical pool

- Discovered: 155694
- Ever alive: 29232
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
