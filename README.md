# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 388
- HTTP: 266 alive / 82 gold
- HTTPS: 153 alive / 22 gold
- SOCKS4: 209 alive / 124 gold
- SOCKS5: 254 alive / 160 gold

## Historical pool

- Discovered: 166560
- Ever alive: 32404
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
