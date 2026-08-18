# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 274
- HTTP: 209 alive / 29 gold
- HTTPS: 146 alive / 5 gold
- SOCKS4: 233 alive / 134 gold
- SOCKS5: 207 alive / 106 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12409
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
