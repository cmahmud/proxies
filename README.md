# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 369
- HTTP: 193 alive / 70 gold
- HTTPS: 151 alive / 22 gold
- SOCKS4: 191 alive / 118 gold
- SOCKS5: 236 alive / 159 gold

## Historical pool

- Discovered: 148331
- Ever alive: 26060
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
