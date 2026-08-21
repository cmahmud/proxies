# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 353
- HTTP: 363 alive / 75 gold
- HTTPS: 206 alive / 17 gold
- SOCKS4: 202 alive / 127 gold
- SOCKS5: 245 alive / 134 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29852
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
