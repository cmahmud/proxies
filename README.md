# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 407
- HTTP: 101 alive / 66 gold
- HTTPS: 177 alive / 17 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41061
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
