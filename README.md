# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 455
- HTTP: 95 alive / 77 gold
- HTTPS: 117 alive / 37 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 196 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47397
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
