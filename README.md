# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 417
- HTTP: 101 alive / 71 gold
- HTTPS: 116 alive / 23 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41974
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
