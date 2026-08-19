# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 533
- HTTP: 374 alive / 157 gold
- HTTPS: 260 alive / 86 gold
- SOCKS4: 231 alive / 150 gold
- SOCKS5: 209 alive / 140 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18060
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
