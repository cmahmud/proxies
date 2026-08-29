# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 394
- HTTP: 93 alive / 68 gold
- HTTPS: 79 alive / 15 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43261
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
