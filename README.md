# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 422
- HTTP: 323 alive / 83 gold
- HTTPS: 243 alive / 21 gold
- SOCKS4: 253 alive / 156 gold
- SOCKS5: 235 alive / 162 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29806
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
