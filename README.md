# SyndProxy private pool

## Current pool

- Alive now: 1187
- Gold now: 440
- HTTP: 432 alive / 101 gold
- HTTPS: 288 alive / 29 gold
- SOCKS4: 204 alive / 140 gold
- SOCKS5: 263 alive / 170 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28722
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
