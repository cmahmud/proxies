# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 531
- HTTP: 355 alive / 167 gold
- HTTPS: 238 alive / 87 gold
- SOCKS4: 203 alive / 136 gold
- SOCKS5: 227 alive / 141 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18650
- Ever gold: 725

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
