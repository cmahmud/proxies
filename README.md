# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 408
- HTTP: 398 alive / 94 gold
- HTTPS: 250 alive / 16 gold
- SOCKS4: 232 alive / 143 gold
- SOCKS5: 259 alive / 155 gold

## Historical pool

- Discovered: 131817
- Ever alive: 20891
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
