# SyndProxy private pool

## Current pool

- Alive now: 1484
- Gold now: 621
- HTTP: 584 alive / 220 gold
- HTTPS: 438 alive / 115 gold
- SOCKS4: 219 alive / 137 gold
- SOCKS5: 243 alive / 149 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23802
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
