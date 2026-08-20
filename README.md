# SyndProxy private pool

## Current pool

- Alive now: 1567
- Gold now: 559
- HTTP: 608 alive / 179 gold
- HTTPS: 368 alive / 85 gold
- SOCKS4: 243 alive / 140 gold
- SOCKS5: 348 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22707
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
