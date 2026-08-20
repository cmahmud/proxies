# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 397
- HTTP: 183 alive / 75 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 209 alive / 154 gold
- SOCKS5: 210 alive / 148 gold

## Historical pool

- Discovered: 149503
- Ever alive: 26755
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
