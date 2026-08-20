# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 388
- HTTP: 251 alive / 70 gold
- HTTPS: 98 alive / 21 gold
- SOCKS4: 192 alive / 149 gold
- SOCKS5: 212 alive / 148 gold

## Historical pool

- Discovered: 146664
- Ever alive: 25748
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
