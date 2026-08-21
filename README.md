# SyndProxy private pool

## Current pool

- Alive now: 1364
- Gold now: 427
- HTTP: 535 alive / 101 gold
- HTTPS: 363 alive / 28 gold
- SOCKS4: 221 alive / 140 gold
- SOCKS5: 245 alive / 158 gold

## Historical pool

- Discovered: 159281
- Ever alive: 30406
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
