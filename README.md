# SyndProxy private pool

## Current pool

- Alive now: 703
- Gold now: 388
- HTTP: 179 alive / 63 gold
- HTTPS: 127 alive / 20 gold
- SOCKS4: 192 alive / 151 gold
- SOCKS5: 205 alive / 154 gold

## Historical pool

- Discovered: 146668
- Ever alive: 25755
- Ever gold: 1075

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
