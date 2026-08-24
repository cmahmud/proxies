# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 388
- HTTP: 130 alive / 57 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33500
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
