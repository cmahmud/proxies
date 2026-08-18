# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 315
- HTTP: 289 alive / 40 gold
- HTTPS: 183 alive / 9 gold
- SOCKS4: 235 alive / 134 gold
- SOCKS5: 222 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14271
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
