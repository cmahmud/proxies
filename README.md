# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 416
- HTTP: 301 alive / 84 gold
- HTTPS: 217 alive / 27 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 243 alive / 161 gold

## Historical pool

- Discovered: 156412
- Ever alive: 29431
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
