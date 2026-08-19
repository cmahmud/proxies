# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 536
- HTTP: 454 alive / 179 gold
- HTTPS: 269 alive / 110 gold
- SOCKS4: 189 alive / 116 gold
- SOCKS5: 186 alive / 131 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19410
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
