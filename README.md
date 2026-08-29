# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 399
- HTTP: 93 alive / 67 gold
- HTTPS: 79 alive / 15 gold
- SOCKS4: 160 alive / 154 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43260
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
