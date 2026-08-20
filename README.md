# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 431
- HTTP: 340 alive / 101 gold
- HTTPS: 271 alive / 24 gold
- SOCKS4: 274 alive / 150 gold
- SOCKS5: 251 alive / 156 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25158
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
