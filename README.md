# SyndProxy private pool

## Current pool

- Alive now: 1141
- Gold now: 533
- HTTP: 424 alive / 161 gold
- HTTPS: 298 alive / 93 gold
- SOCKS4: 206 alive / 136 gold
- SOCKS5: 213 alive / 143 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19858
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
