# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 374
- HTTP: 200 alive / 87 gold
- HTTPS: 174 alive / 30 gold
- SOCKS4: 189 alive / 112 gold
- SOCKS5: 219 alive / 145 gold

## Historical pool

- Discovered: 163856
- Ever alive: 31950
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
