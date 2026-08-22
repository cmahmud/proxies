# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 433
- HTTP: 286 alive / 88 gold
- HTTPS: 209 alive / 31 gold
- SOCKS4: 202 alive / 151 gold
- SOCKS5: 242 alive / 163 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31533
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
