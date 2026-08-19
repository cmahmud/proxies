# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 529
- HTTP: 348 alive / 162 gold
- HTTPS: 245 alive / 89 gold
- SOCKS4: 212 alive / 134 gold
- SOCKS5: 225 alive / 144 gold

## Historical pool

- Discovered: 123075
- Ever alive: 18701
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
