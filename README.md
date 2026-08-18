# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 210
- HTTP: 222 alive / 23 gold
- HTTPS: 170 alive / 8 gold
- SOCKS4: 191 alive / 96 gold
- SOCKS5: 223 alive / 83 gold

## Historical pool

- Discovered: 91698
- Ever alive: 8628
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
