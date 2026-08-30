# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 421
- HTTP: 134 alive / 81 gold
- HTTPS: 78 alive / 29 gold
- SOCKS4: 157 alive / 151 gold
- SOCKS5: 217 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43965
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
