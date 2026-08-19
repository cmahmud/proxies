# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 538
- HTTP: 432 alive / 160 gold
- HTTPS: 287 alive / 90 gold
- SOCKS4: 230 alive / 143 gold
- SOCKS5: 204 alive / 145 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19152
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
