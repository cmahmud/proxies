# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 408
- HTTP: 363 alive / 95 gold
- HTTPS: 270 alive / 15 gold
- SOCKS4: 240 alive / 150 gold
- SOCKS5: 308 alive / 148 gold

## Historical pool

- Discovered: 131836
- Ever alive: 21124
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
