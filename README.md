# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 276
- HTTP: 185 alive / 28 gold
- HTTPS: 145 alive / 5 gold
- SOCKS4: 235 alive / 136 gold
- SOCKS5: 208 alive / 107 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12409
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
