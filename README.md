# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 449
- HTTP: 328 alive / 108 gold
- HTTPS: 205 alive / 31 gold
- SOCKS4: 219 alive / 151 gold
- SOCKS5: 252 alive / 159 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28583
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
