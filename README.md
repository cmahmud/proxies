# SyndProxy private pool

## Current pool

- Alive now: 1416
- Gold now: 572
- HTTP: 582 alive / 188 gold
- HTTPS: 375 alive / 89 gold
- SOCKS4: 216 alive / 132 gold
- SOCKS5: 243 alive / 163 gold

## Historical pool

- Discovered: 138835
- Ever alive: 23078
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
