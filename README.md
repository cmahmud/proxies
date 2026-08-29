# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 293
- HTTP: 50 alive / 25 gold
- HTTPS: 5 alive / 1 gold
- SOCKS4: 159 alive / 139 gold
- SOCKS5: 170 alive / 128 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43595
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
