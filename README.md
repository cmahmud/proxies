# SyndProxy private pool

## Current pool

- Alive now: 1257
- Gold now: 519
- HTTP: 478 alive / 183 gold
- HTTPS: 336 alive / 55 gold
- SOCKS4: 204 alive / 122 gold
- SOCKS5: 239 alive / 159 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19650
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
