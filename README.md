# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 532
- HTTP: 336 alive / 161 gold
- HTTPS: 243 alive / 88 gold
- SOCKS4: 232 alive / 151 gold
- SOCKS5: 202 alive / 132 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18081
- Ever gold: 715

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
