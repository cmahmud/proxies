# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 461
- HTTP: 295 alive / 115 gold
- HTTPS: 197 alive / 87 gold
- SOCKS4: 205 alive / 125 gold
- SOCKS5: 219 alive / 134 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17494
- Ever gold: 666

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
