# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 471
- HTTP: 398 alive / 121 gold
- HTTPS: 269 alive / 74 gold
- SOCKS4: 232 alive / 142 gold
- SOCKS5: 251 alive / 134 gold

## Historical pool

- Discovered: 113533
- Ever alive: 16446
- Ever gold: 620

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
