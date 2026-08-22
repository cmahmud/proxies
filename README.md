# SyndProxy private pool

## Current pool

- Alive now: 851
- Gold now: 406
- HTTP: 226 alive / 90 gold
- HTTPS: 174 alive / 29 gold
- SOCKS4: 215 alive / 133 gold
- SOCKS5: 236 alive / 154 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31944
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
