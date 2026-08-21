# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 401
- HTTP: 354 alive / 80 gold
- HTTPS: 226 alive / 23 gold
- SOCKS4: 240 alive / 147 gold
- SOCKS5: 283 alive / 151 gold

## Historical pool

- Discovered: 156433
- Ever alive: 29538
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
