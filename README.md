# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 362
- HTTP: 73 alive / 39 gold
- HTTPS: 33 alive / 11 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 177 alive / 159 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
