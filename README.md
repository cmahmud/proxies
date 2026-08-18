# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 295
- HTTP: 302 alive / 34 gold
- HTTPS: 193 alive / 6 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 215 alive / 126 gold

## Historical pool

- Discovered: 102846
- Ever alive: 13209
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
