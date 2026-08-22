# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 406
- HTTP: 221 alive / 92 gold
- HTTPS: 180 alive / 30 gold
- SOCKS4: 214 alive / 131 gold
- SOCKS5: 232 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31938
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
