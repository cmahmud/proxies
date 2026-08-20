# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 363
- HTTP: 203 alive / 83 gold
- HTTPS: 130 alive / 21 gold
- SOCKS4: 225 alive / 133 gold
- SOCKS5: 201 alive / 126 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26603
- Ever gold: 1083

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
