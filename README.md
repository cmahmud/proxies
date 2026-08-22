# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 437
- HTTP: 346 alive / 96 gold
- HTTPS: 234 alive / 27 gold
- SOCKS4: 204 alive / 144 gold
- SOCKS5: 261 alive / 170 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31250
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
