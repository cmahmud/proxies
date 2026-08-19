# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 532
- HTTP: 362 alive / 163 gold
- HTTPS: 232 alive / 89 gold
- SOCKS4: 220 alive / 133 gold
- SOCKS5: 215 alive / 147 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18727
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
