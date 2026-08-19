# SyndProxy private pool

## Current pool

- Alive now: 1288
- Gold now: 533
- HTTP: 473 alive / 184 gold
- HTTPS: 344 alive / 60 gold
- SOCKS4: 222 alive / 123 gold
- SOCKS5: 249 alive / 166 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19659
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
