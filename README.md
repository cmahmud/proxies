# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 383
- HTTP: 332 alive / 80 gold
- HTTPS: 226 alive / 24 gold
- SOCKS4: 223 alive / 124 gold
- SOCKS5: 244 alive / 155 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
