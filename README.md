# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 426
- HTTP: 346 alive / 87 gold
- HTTPS: 206 alive / 24 gold
- SOCKS4: 222 alive / 155 gold
- SOCKS5: 257 alive / 160 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30224
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
