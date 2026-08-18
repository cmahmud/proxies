# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 232
- HTTP: 170 alive / 29 gold
- HTTPS: 94 alive / 7 gold
- SOCKS4: 197 alive / 113 gold
- SOCKS5: 203 alive / 83 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7595
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
