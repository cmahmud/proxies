# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 416
- HTTP: 106 alive / 69 gold
- HTTPS: 130 alive / 18 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41332
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
