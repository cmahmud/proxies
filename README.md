# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 276
- HTTP: 187 alive / 29 gold
- HTTPS: 151 alive / 5 gold
- SOCKS4: 239 alive / 135 gold
- SOCKS5: 206 alive / 107 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12409
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
