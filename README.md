# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 378
- HTTP: 338 alive / 86 gold
- HTTPS: 244 alive / 24 gold
- SOCKS4: 211 alive / 132 gold
- SOCKS5: 230 alive / 136 gold

## Historical pool

- Discovered: 165018
- Ever alive: 32269
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
