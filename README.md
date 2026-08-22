# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 445
- HTTP: 306 alive / 95 gold
- HTTPS: 230 alive / 29 gold
- SOCKS4: 225 alive / 160 gold
- SOCKS5: 268 alive / 161 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31016
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
