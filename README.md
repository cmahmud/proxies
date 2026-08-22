# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 344
- HTTP: 295 alive / 82 gold
- HTTPS: 237 alive / 30 gold
- SOCKS4: 193 alive / 138 gold
- SOCKS5: 194 alive / 94 gold

## Historical pool

- Discovered: 167111
- Ever alive: 32515
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
