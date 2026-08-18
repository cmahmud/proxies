# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 224
- HTTP: 268 alive / 29 gold
- HTTPS: 102 alive / 8 gold
- SOCKS4: 202 alive / 116 gold
- SOCKS5: 209 alive / 71 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9302
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
