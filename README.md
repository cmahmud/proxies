# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 397
- HTTP: 251 alive / 87 gold
- HTTPS: 154 alive / 22 gold
- SOCKS4: 194 alive / 132 gold
- SOCKS5: 233 alive / 156 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27676
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
