# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 366
- HTTP: 195 alive / 84 gold
- HTTPS: 150 alive / 20 gold
- SOCKS4: 222 alive / 134 gold
- SOCKS5: 213 alive / 128 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26613
- Ever gold: 1084

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
