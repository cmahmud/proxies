# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 379
- HTTP: 196 alive / 74 gold
- HTTPS: 155 alive / 17 gold
- SOCKS4: 217 alive / 145 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26287
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
