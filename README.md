# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 541
- HTTP: 416 alive / 169 gold
- HTTPS: 265 alive / 90 gold
- SOCKS4: 218 alive / 133 gold
- SOCKS5: 222 alive / 149 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18738
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
