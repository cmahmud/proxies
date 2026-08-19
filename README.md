# SyndProxy private pool

## Current pool

- Alive now: 1349
- Gold now: 592
- HTTP: 521 alive / 182 gold
- HTTPS: 352 alive / 111 gold
- SOCKS4: 241 alive / 143 gold
- SOCKS5: 235 alive / 156 gold

## Historical pool

- Discovered: 125593
- Ever alive: 19554
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
