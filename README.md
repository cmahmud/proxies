# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 382
- HTTP: 196 alive / 61 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 218 alive / 157 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
