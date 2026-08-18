# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 206
- HTTP: 348 alive / 23 gold
- HTTPS: 165 alive / 9 gold
- SOCKS4: 213 alive / 96 gold
- SOCKS5: 225 alive / 78 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7957
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
