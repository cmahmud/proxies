# SyndProxy validated proxy pool

## Current pool

- Alive now: 383
- Gold now: 266
- HTTP: 50 alive / 23 gold
- HTTPS: 5 alive / 0 gold
- SOCKS4: 160 alive / 130 gold
- SOCKS5: 168 alive / 113 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43596
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
