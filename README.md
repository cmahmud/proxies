# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 397
- HTTP: 241 alive / 85 gold
- HTTPS: 138 alive / 19 gold
- SOCKS4: 227 alive / 145 gold
- SOCKS5: 221 alive / 148 gold

## Historical pool

- Discovered: 155802
- Ever alive: 29404
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
