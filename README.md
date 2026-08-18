# SyndProxy private pool

## Current pool

- Alive now: 787
- Gold now: 217
- HTTP: 268 alive / 30 gold
- HTTPS: 116 alive / 8 gold
- SOCKS4: 217 alive / 102 gold
- SOCKS5: 186 alive / 77 gold

## Historical pool

- Discovered: 86694
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
