# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 398
- HTTP: 102 alive / 71 gold
- HTTPS: 80 alive / 12 gold
- SOCKS4: 159 alive / 155 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43096
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
