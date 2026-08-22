# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 383
- HTTP: 375 alive / 81 gold
- HTTPS: 244 alive / 24 gold
- SOCKS4: 222 alive / 124 gold
- SOCKS5: 243 alive / 154 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
