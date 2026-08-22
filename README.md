# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 343
- HTTP: 347 alive / 88 gold
- HTTPS: 256 alive / 24 gold
- SOCKS4: 201 alive / 140 gold
- SOCKS5: 194 alive / 91 gold

## Historical pool

- Discovered: 166948
- Ever alive: 32487
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
