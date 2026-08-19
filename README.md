# SyndProxy private pool

## Current pool

- Alive now: 816
- Gold now: 366
- HTTP: 233 alive / 87 gold
- HTTPS: 170 alive / 16 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 203 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18287
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
