# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 417
- HTTP: 281 alive / 85 gold
- HTTPS: 200 alive / 27 gold
- SOCKS4: 189 alive / 136 gold
- SOCKS5: 260 alive / 169 gold

## Historical pool

- Discovered: 161926
- Ever alive: 31194
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
