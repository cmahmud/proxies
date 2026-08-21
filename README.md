# SyndProxy private pool

## Current pool

- Alive now: 1418
- Gold now: 447
- HTTP: 536 alive / 104 gold
- HTTPS: 367 alive / 28 gold
- SOCKS4: 240 alive / 152 gold
- SOCKS5: 275 alive / 163 gold

## Historical pool

- Discovered: 159335
- Ever alive: 30478
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
