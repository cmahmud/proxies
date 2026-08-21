# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 390
- HTTP: 261 alive / 82 gold
- HTTPS: 158 alive / 23 gold
- SOCKS4: 184 alive / 127 gold
- SOCKS5: 244 alive / 158 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29687
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
