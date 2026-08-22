# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 397
- HTTP: 284 alive / 90 gold
- HTTPS: 191 alive / 25 gold
- SOCKS4: 214 alive / 148 gold
- SOCKS5: 212 alive / 134 gold

## Historical pool

- Discovered: 165826
- Ever alive: 32348
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
