# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 371
- HTTP: 183 alive / 72 gold
- HTTPS: 145 alive / 18 gold
- SOCKS4: 213 alive / 139 gold
- SOCKS5: 202 alive / 142 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26281
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
