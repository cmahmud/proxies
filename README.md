# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 419
- HTTP: 104 alive / 63 gold
- HTTPS: 75 alive / 21 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35991
- Ever gold: 1262

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
