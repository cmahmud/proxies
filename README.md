# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 485
- HTTP: 323 alive / 145 gold
- HTTPS: 257 alive / 87 gold
- SOCKS4: 198 alive / 122 gold
- SOCKS5: 209 alive / 131 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17606
- Ever gold: 690

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
