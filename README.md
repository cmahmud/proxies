# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 519
- HTTP: 326 alive / 156 gold
- HTTPS: 245 alive / 88 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 197 alive / 134 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18471
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
