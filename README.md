# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 420
- HTTP: 305 alive / 87 gold
- HTTPS: 217 alive / 27 gold
- SOCKS4: 216 alive / 145 gold
- SOCKS5: 242 alive / 161 gold

## Historical pool

- Discovered: 156412
- Ever alive: 29431
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
