# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 448
- HTTP: 100 alive / 78 gold
- HTTPS: 108 alive / 31 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47388
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
