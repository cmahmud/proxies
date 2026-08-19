# SyndProxy private pool

## Current pool

- Alive now: 1342
- Gold now: 369
- HTTP: 428 alive / 82 gold
- HTTPS: 302 alive / 14 gold
- SOCKS4: 266 alive / 138 gold
- SOCKS5: 346 alive / 135 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21472
- Ever gold: 882

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
