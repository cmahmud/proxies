# SyndProxy private pool

## Current pool

- Alive now: 1892
- Gold now: 653
- HTTP: 745 alive / 234 gold
- HTTPS: 619 alive / 119 gold
- SOCKS4: 232 alive / 145 gold
- SOCKS5: 296 alive / 155 gold

## Historical pool

- Discovered: 142693
- Ever alive: 24292
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
