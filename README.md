# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 273
- HTTP: 262 alive / 32 gold
- HTTPS: 124 alive / 5 gold
- SOCKS4: 210 alive / 132 gold
- SOCKS5: 214 alive / 104 gold

## Historical pool

- Discovered: 99053
- Ever alive: 11134
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
