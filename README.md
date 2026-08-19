# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 514
- HTTP: 397 alive / 155 gold
- HTTPS: 282 alive / 86 gold
- SOCKS4: 205 alive / 141 gold
- SOCKS5: 200 alive / 132 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18497
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
