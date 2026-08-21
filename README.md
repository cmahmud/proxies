# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 407
- HTTP: 248 alive / 86 gold
- HTTPS: 174 alive / 22 gold
- SOCKS4: 194 alive / 137 gold
- SOCKS5: 254 alive / 162 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29045
- Ever gold: 1121

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
