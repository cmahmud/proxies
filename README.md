# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 344
- HTTP: 277 alive / 51 gold
- HTTPS: 187 alive / 11 gold
- SOCKS4: 231 alive / 142 gold
- SOCKS5: 219 alive / 140 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
