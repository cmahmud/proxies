# SyndProxy private pool

## Current pool

- Alive now: 1473
- Gold now: 425
- HTTP: 565 alive / 114 gold
- HTTPS: 343 alive / 21 gold
- SOCKS4: 243 alive / 137 gold
- SOCKS5: 322 alive / 153 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22676
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
