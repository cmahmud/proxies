# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 349
- HTTP: 64 alive / 37 gold
- HTTPS: 35 alive / 6 gold
- SOCKS4: 160 alive / 145 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43586
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
