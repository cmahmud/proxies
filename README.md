# SyndProxy private pool

## Current pool

- Alive now: 1183
- Gold now: 390
- HTTP: 384 alive / 91 gold
- HTTPS: 271 alive / 21 gold
- SOCKS4: 225 alive / 127 gold
- SOCKS5: 303 alive / 151 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22144
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
