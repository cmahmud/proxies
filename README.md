# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 382
- HTTP: 208 alive / 80 gold
- HTTPS: 146 alive / 21 gold
- SOCKS4: 186 alive / 130 gold
- SOCKS5: 205 alive / 151 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31342
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
