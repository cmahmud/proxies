# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 334
- HTTP: 283 alive / 44 gold
- HTTPS: 201 alive / 10 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 230 alive / 138 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14554
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
