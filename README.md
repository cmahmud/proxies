# SyndProxy private pool

## Current pool

- Alive now: 1174
- Gold now: 406
- HTTP: 373 alive / 94 gold
- HTTPS: 257 alive / 14 gold
- SOCKS4: 239 alive / 150 gold
- SOCKS5: 305 alive / 148 gold

## Historical pool

- Discovered: 131840
- Ever alive: 21153
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
