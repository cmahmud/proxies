# SyndProxy private pool

## Current pool

- Alive now: 1559
- Gold now: 595
- HTTP: 608 alive / 190 gold
- HTTPS: 483 alive / 91 gold
- SOCKS4: 224 alive / 144 gold
- SOCKS5: 244 alive / 170 gold

## Historical pool

- Discovered: 141227
- Ever alive: 23993
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
