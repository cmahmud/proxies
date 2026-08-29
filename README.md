# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 395
- HTTP: 86 alive / 68 gold
- HTTPS: 83 alive / 15 gold
- SOCKS4: 156 alive / 152 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43242
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
