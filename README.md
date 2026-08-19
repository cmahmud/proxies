# SyndProxy private pool

## Current pool

- Alive now: 1361
- Gold now: 400
- HTTP: 473 alive / 90 gold
- HTTPS: 313 alive / 17 gold
- SOCKS4: 257 alive / 146 gold
- SOCKS5: 318 alive / 147 gold

## Historical pool

- Discovered: 133965
- Ever alive: 21667
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
