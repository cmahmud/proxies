# SyndProxy private pool

## Current pool

- Alive now: 723
- Gold now: 384
- HTTP: 166 alive / 75 gold
- HTTPS: 136 alive / 20 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 196 alive / 139 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26245
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
