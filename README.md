# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 350
- HTTP: 388 alive / 49 gold
- HTTPS: 219 alive / 14 gold
- SOCKS4: 241 alive / 147 gold
- SOCKS5: 226 alive / 140 gold

## Historical pool

- Discovered: 107085
- Ever alive: 14855
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
