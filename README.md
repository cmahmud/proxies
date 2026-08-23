# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 370
- HTTP: 70 alive / 37 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
