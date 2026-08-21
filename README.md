# SyndProxy private pool

## Current pool

- Alive now: 1229
- Gold now: 454
- HTTP: 445 alive / 102 gold
- HTTPS: 299 alive / 30 gold
- SOCKS4: 217 alive / 153 gold
- SOCKS5: 268 alive / 169 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28729
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
