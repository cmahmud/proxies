# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 397
- HTTP: 396 alive / 91 gold
- HTTPS: 268 alive / 23 gold
- SOCKS4: 206 alive / 142 gold
- SOCKS5: 243 alive / 141 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28806
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
