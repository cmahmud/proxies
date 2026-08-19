# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 367
- HTTP: 231 alive / 88 gold
- HTTPS: 164 alive / 16 gold
- SOCKS4: 206 alive / 139 gold
- SOCKS5: 203 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18287
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
