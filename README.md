# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 394
- HTTP: 315 alive / 86 gold
- HTTPS: 206 alive / 23 gold
- SOCKS4: 199 alive / 130 gold
- SOCKS5: 271 alive / 155 gold

## Historical pool

- Discovered: 144740
- Ever alive: 24998
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
