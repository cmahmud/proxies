# SyndProxy private pool

## Current pool

- Alive now: 683
- Gold now: 257
- HTTP: 208 alive / 31 gold
- HTTPS: 84 alive / 7 gold
- SOCKS4: 195 alive / 132 gold
- SOCKS5: 196 alive / 87 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9147
- Ever gold: 363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
