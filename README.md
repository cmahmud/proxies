# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 357
- HTTP: 324 alive / 76 gold
- HTTPS: 194 alive / 19 gold
- SOCKS4: 204 alive / 127 gold
- SOCKS5: 248 alive / 135 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29852
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
