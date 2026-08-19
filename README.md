# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 531
- HTTP: 325 alive / 158 gold
- HTTPS: 260 alive / 87 gold
- SOCKS4: 233 alive / 154 gold
- SOCKS5: 203 alive / 132 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18123
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
