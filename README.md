# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 387
- HTTP: 273 alive / 78 gold
- HTTPS: 217 alive / 26 gold
- SOCKS4: 208 alive / 125 gold
- SOCKS5: 232 alive / 158 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32249
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
