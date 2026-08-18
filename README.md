# SyndProxy private pool

## Current pool

- Alive now: 1105
- Gold now: 252
- HTTP: 428 alive / 24 gold
- HTTPS: 246 alive / 10 gold
- SOCKS4: 214 alive / 122 gold
- SOCKS5: 217 alive / 96 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10143
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
