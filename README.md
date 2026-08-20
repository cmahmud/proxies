# SyndProxy private pool

## Current pool

- Alive now: 1364
- Gold now: 576
- HTTP: 476 alive / 189 gold
- HTTPS: 362 alive / 98 gold
- SOCKS4: 252 alive / 138 gold
- SOCKS5: 274 alive / 151 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23291
- Ever gold: 916

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
