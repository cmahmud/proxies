# SyndProxy private pool

## Current pool

- Alive now: 718
- Gold now: 245
- HTTP: 197 alive / 27 gold
- HTTPS: 124 alive / 9 gold
- SOCKS4: 180 alive / 107 gold
- SOCKS5: 217 alive / 102 gold

## Historical pool

- Discovered: 95227
- Ever alive: 10179
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
