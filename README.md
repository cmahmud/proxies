# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 509
- HTTP: 401 alive / 146 gold
- HTTPS: 324 alive / 93 gold
- SOCKS4: 210 alive / 129 gold
- SOCKS5: 253 alive / 141 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17339
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
