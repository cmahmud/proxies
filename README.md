# SyndProxy private pool

## Current pool

- Alive now: 728
- Gold now: 412
- HTTP: 188 alive / 86 gold
- HTTPS: 125 alive / 27 gold
- SOCKS4: 200 alive / 140 gold
- SOCKS5: 215 alive / 159 gold

## Historical pool

- Discovered: 162439
- Ever alive: 31423
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
