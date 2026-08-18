# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 261
- HTTP: 279 alive / 30 gold
- HTTPS: 126 alive / 4 gold
- SOCKS4: 206 alive / 118 gold
- SOCKS5: 211 alive / 109 gold

## Historical pool

- Discovered: 99142
- Ever alive: 11979
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
