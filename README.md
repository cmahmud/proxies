# SyndProxy private pool

## Current pool

- Alive now: 1627
- Gold now: 635
- HTTP: 572 alive / 211 gold
- HTTPS: 456 alive / 116 gold
- SOCKS4: 244 alive / 150 gold
- SOCKS5: 355 alive / 158 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24094
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
