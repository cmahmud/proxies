# SyndProxy private pool

## Current pool

- Alive now: 1300
- Gold now: 447
- HTTP: 446 alive / 103 gold
- HTTPS: 314 alive / 32 gold
- SOCKS4: 253 alive / 151 gold
- SOCKS5: 287 alive / 161 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30457
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
