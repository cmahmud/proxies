# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 386
- HTTP: 199 alive / 79 gold
- HTTPS: 128 alive / 24 gold
- SOCKS4: 195 alive / 136 gold
- SOCKS5: 243 alive / 147 gold

## Historical pool

- Discovered: 147687
- Ever alive: 25955
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
