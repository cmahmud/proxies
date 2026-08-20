# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 363
- HTTP: 201 alive / 82 gold
- HTTPS: 135 alive / 20 gold
- SOCKS4: 216 alive / 134 gold
- SOCKS5: 202 alive / 127 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26602
- Ever gold: 1083

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
