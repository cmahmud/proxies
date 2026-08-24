# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 379
- HTTP: 95 alive / 48 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33498
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
