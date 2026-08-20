# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 376
- HTTP: 311 alive / 88 gold
- HTTPS: 254 alive / 25 gold
- SOCKS4: 206 alive / 130 gold
- SOCKS5: 258 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25047
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
