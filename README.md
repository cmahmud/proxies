# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 408
- HTTP: 106 alive / 64 gold
- HTTPS: 156 alive / 15 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41218
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
