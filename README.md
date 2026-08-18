# SyndProxy private pool

## Current pool

- Alive now: 628
- Gold now: 234
- HTTP: 160 alive / 29 gold
- HTTPS: 85 alive / 8 gold
- SOCKS4: 189 alive / 114 gold
- SOCKS5: 194 alive / 83 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7595
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
