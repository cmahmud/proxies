# SyndProxy private pool

## Current pool

- Alive now: 1730
- Gold now: 642
- HTTP: 683 alive / 220 gold
- HTTPS: 502 alive / 116 gold
- SOCKS4: 215 alive / 147 gold
- SOCKS5: 330 alive / 159 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24198
- Ever gold: 971

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
