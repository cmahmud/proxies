# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 451
- HTTP: 421 alive / 101 gold
- HTTPS: 299 alive / 29 gold
- SOCKS4: 213 alive / 151 gold
- SOCKS5: 262 alive / 170 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28728
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
