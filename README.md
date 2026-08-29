# SyndProxy validated proxy pool

## Current pool

- Alive now: 438
- Gold now: 349
- HTTP: 84 alive / 45 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 156 alive / 148 gold
- SOCKS5: 155 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43641
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
