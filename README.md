# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 347
- HTTP: 167 alive / 63 gold
- HTTPS: 119 alive / 18 gold
- SOCKS4: 166 alive / 130 gold
- SOCKS5: 189 alive / 136 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25755
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
