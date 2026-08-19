# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 398
- HTTP: 400 alive / 89 gold
- HTTPS: 288 alive / 21 gold
- SOCKS4: 225 alive / 136 gold
- SOCKS5: 288 alive / 152 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22166
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
