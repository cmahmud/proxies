# SyndProxy private pool

## Current pool

- Alive now: 1071
- Gold now: 284
- HTTP: 406 alive / 30 gold
- HTTPS: 182 alive / 4 gold
- SOCKS4: 248 alive / 137 gold
- SOCKS5: 235 alive / 113 gold

## Historical pool

- Discovered: 100097
- Ever alive: 12657
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
