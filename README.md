# SyndProxy private pool

## Current pool

- Alive now: 1854
- Gold now: 651
- HTTP: 703 alive / 230 gold
- HTTPS: 599 alive / 120 gold
- SOCKS4: 246 alive / 146 gold
- SOCKS5: 306 alive / 155 gold

## Historical pool

- Discovered: 142695
- Ever alive: 24302
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
