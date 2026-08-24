# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 379
- HTTP: 93 alive / 51 gold
- HTTPS: 38 alive / 13 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 197 alive / 160 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33346
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
