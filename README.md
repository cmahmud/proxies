# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 377
- HTTP: 94 alive / 51 gold
- HTTPS: 38 alive / 12 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 196 alive / 160 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33346
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
