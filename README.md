# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 387
- HTTP: 379 alive / 91 gold
- HTTPS: 251 alive / 23 gold
- SOCKS4: 194 alive / 135 gold
- SOCKS5: 239 alive / 138 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28804
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
