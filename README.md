# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 398
- HTTP: 276 alive / 73 gold
- HTTPS: 145 alive / 22 gold
- SOCKS4: 243 alive / 162 gold
- SOCKS5: 239 alive / 141 gold

## Historical pool

- Discovered: 156825
- Ever alive: 29617
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
