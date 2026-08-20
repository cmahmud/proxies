# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 397
- HTTP: 287 alive / 83 gold
- HTTPS: 209 alive / 26 gold
- SOCKS4: 193 alive / 134 gold
- SOCKS5: 245 alive / 154 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24962
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
