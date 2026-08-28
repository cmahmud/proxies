# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 412
- HTTP: 99 alive / 68 gold
- HTTPS: 100 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42604
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
