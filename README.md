# SyndProxy private pool

## Current pool

- Alive now: 1559
- Gold now: 627
- HTTP: 639 alive / 247 gold
- HTTPS: 500 alive / 117 gold
- SOCKS4: 176 alive / 104 gold
- SOCKS5: 244 alive / 159 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24733
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
