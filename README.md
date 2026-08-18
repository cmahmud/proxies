# SyndProxy private pool

## Current pool

- Alive now: 629
- Gold now: 242
- HTTP: 159 alive / 32 gold
- HTTPS: 79 alive / 8 gold
- SOCKS4: 195 alive / 114 gold
- SOCKS5: 196 alive / 88 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7595
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
