# SyndProxy private pool

## Current pool

- Alive now: 625
- Gold now: 234
- HTTP: 157 alive / 29 gold
- HTTPS: 83 alive / 8 gold
- SOCKS4: 192 alive / 114 gold
- SOCKS5: 193 alive / 83 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7595
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
