# SyndProxy private pool

## Current pool

- Alive now: 1330
- Gold now: 529
- HTTP: 515 alive / 188 gold
- HTTPS: 343 alive / 47 gold
- SOCKS4: 226 alive / 134 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 125596
- Ever alive: 19577
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
