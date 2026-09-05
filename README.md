# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 304
- HTTP: 103 alive / 75 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 77 alive / 70 gold
- SOCKS5: 171 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47835
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
