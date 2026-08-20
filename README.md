# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 378
- HTTP: 204 alive / 69 gold
- HTTPS: 136 alive / 15 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 212 alive / 150 gold

## Historical pool

- Discovered: 145549
- Ever alive: 25403
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
