# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 388
- HTTP: 110 alive / 56 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 193 alive / 161 gold

## Historical pool

- Discovered: 178284
- Ever alive: 33365
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
