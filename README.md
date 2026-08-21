# SyndProxy private pool

## Current pool

- Alive now: 1178
- Gold now: 397
- HTTP: 398 alive / 99 gold
- HTTPS: 308 alive / 26 gold
- SOCKS4: 219 alive / 127 gold
- SOCKS5: 253 alive / 145 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28115
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
