# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 448
- HTTP: 324 alive / 105 gold
- HTTPS: 209 alive / 35 gold
- SOCKS4: 188 alive / 148 gold
- SOCKS5: 267 alive / 160 gold

## Historical pool

- Discovered: 153732
- Ever alive: 28677
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
