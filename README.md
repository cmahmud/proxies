# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 378
- HTTP: 182 alive / 75 gold
- HTTPS: 133 alive / 18 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 220 alive / 140 gold

## Historical pool

- Discovered: 148338
- Ever alive: 26318
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
