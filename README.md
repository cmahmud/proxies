# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 409
- HTTP: 357 alive / 87 gold
- HTTPS: 238 alive / 32 gold
- SOCKS4: 218 alive / 133 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 163042
- Ever alive: 31687
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
