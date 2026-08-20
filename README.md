# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 360
- HTTP: 184 alive / 66 gold
- HTTPS: 141 alive / 19 gold
- SOCKS4: 185 alive / 135 gold
- SOCKS5: 191 alive / 140 gold

## Historical pool

- Discovered: 149498
- Ever alive: 26687
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
