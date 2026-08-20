# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 397
- HTTP: 166 alive / 71 gold
- HTTPS: 154 alive / 22 gold
- SOCKS4: 199 alive / 154 gold
- SOCKS5: 209 alive / 150 gold

## Historical pool

- Discovered: 149503
- Ever alive: 26767
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
