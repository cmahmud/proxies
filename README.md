# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 347
- HTTP: 304 alive / 67 gold
- HTTPS: 190 alive / 15 gold
- SOCKS4: 227 alive / 141 gold
- SOCKS5: 205 alive / 124 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15286
- Ever gold: 491

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
