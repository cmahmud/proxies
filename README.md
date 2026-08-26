# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 400
- HTTP: 127 alive / 72 gold
- HTTPS: 156 alive / 24 gold
- SOCKS4: 167 alive / 148 gold
- SOCKS5: 184 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40141
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
