# SyndProxy private pool

## Current pool

- Alive now: 1105
- Gold now: 446
- HTTP: 379 alive / 99 gold
- HTTPS: 251 alive / 30 gold
- SOCKS4: 206 alive / 149 gold
- SOCKS5: 269 alive / 168 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28737
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
