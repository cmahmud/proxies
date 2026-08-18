# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 345
- HTTP: 273 alive / 52 gold
- HTTPS: 178 alive / 11 gold
- SOCKS4: 220 alive / 142 gold
- SOCKS5: 220 alive / 140 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14447
- Ever gold: 464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
