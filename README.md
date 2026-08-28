# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 391
- HTTP: 64 alive / 50 gold
- HTTPS: 62 alive / 18 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42765
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
