# SyndProxy private pool

## Current pool

- Alive now: 1439
- Gold now: 583
- HTTP: 518 alive / 197 gold
- HTTPS: 398 alive / 98 gold
- SOCKS4: 234 alive / 140 gold
- SOCKS5: 289 alive / 148 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23384
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
