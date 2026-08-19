# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 377
- HTTP: 335 alive / 75 gold
- HTTPS: 212 alive / 18 gold
- SOCKS4: 202 alive / 126 gold
- SOCKS5: 245 alive / 158 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15791
- Ever gold: 505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
