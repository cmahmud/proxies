# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 407
- HTTP: 88 alive / 58 gold
- HTTPS: 94 alive / 20 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41496
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
