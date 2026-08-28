# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 411
- HTTP: 93 alive / 68 gold
- HTTPS: 99 alive / 13 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42575
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
