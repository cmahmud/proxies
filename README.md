# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 397
- HTTP: 311 alive / 78 gold
- HTTPS: 197 alive / 23 gold
- SOCKS4: 207 alive / 145 gold
- SOCKS5: 250 alive / 151 gold

## Historical pool

- Discovered: 158236
- Ever alive: 29978
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
