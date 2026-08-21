# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 367
- HTTP: 270 alive / 97 gold
- HTTPS: 179 alive / 27 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 204 alive / 106 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28974
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
