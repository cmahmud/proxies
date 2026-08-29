# SyndProxy validated proxy pool

## Current pool

- Alive now: 387
- Gold now: 269
- HTTP: 51 alive / 25 gold
- HTTPS: 6 alive / 2 gold
- SOCKS4: 160 alive / 125 gold
- SOCKS5: 170 alive / 117 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43595
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
