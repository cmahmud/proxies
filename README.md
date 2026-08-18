# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 219
- HTTP: 276 alive / 32 gold
- HTTPS: 149 alive / 8 gold
- SOCKS4: 244 alive / 103 gold
- SOCKS5: 187 alive / 76 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
