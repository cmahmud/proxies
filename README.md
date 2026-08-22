# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 445
- HTTP: 299 alive / 98 gold
- HTTPS: 223 alive / 33 gold
- SOCKS4: 213 alive / 146 gold
- SOCKS5: 270 alive / 168 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31059
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
