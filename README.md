# SyndProxy private pool

## Current pool

- Alive now: 1380
- Gold now: 408
- HTTP: 483 alive / 78 gold
- HTTPS: 334 alive / 16 gold
- SOCKS4: 251 alive / 156 gold
- SOCKS5: 312 alive / 158 gold

## Historical pool

- Discovered: 134532
- Ever alive: 21951
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
