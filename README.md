# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 417
- HTTP: 99 alive / 71 gold
- HTTPS: 112 alive / 18 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42567
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
