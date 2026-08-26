# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 379
- HTTP: 140 alive / 63 gold
- HTTPS: 170 alive / 19 gold
- SOCKS4: 164 alive / 146 gold
- SOCKS5: 179 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39709
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
