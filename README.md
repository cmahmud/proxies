# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 418
- HTTP: 271 alive / 87 gold
- HTTPS: 256 alive / 26 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 240 alive / 161 gold

## Historical pool

- Discovered: 156412
- Ever alive: 29432
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
