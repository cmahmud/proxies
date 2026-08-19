# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 498
- HTTP: 433 alive / 178 gold
- HTTPS: 243 alive / 100 gold
- SOCKS4: 215 alive / 109 gold
- SOCKS5: 186 alive / 111 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19339
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
