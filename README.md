# SyndProxy private pool

## Current pool

- Alive now: 1760
- Gold now: 611
- HTTP: 782 alive / 204 gold
- HTTPS: 569 alive / 142 gold
- SOCKS4: 180 alive / 101 gold
- SOCKS5: 229 alive / 164 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24710
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
