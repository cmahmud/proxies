# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 377
- HTTP: 101 alive / 60 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 160 alive / 153 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 175898
- Ever alive: 33200
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
