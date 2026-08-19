# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 552
- HTTP: 393 alive / 181 gold
- HTTPS: 280 alive / 115 gold
- SOCKS4: 201 alive / 120 gold
- SOCKS5: 203 alive / 136 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19320
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
