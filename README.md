# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 403
- HTTP: 219 alive / 91 gold
- HTTPS: 150 alive / 29 gold
- SOCKS4: 209 alive / 130 gold
- SOCKS5: 232 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31934
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
