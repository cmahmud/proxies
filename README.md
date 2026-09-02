# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 444
- HTTP: 108 alive / 82 gold
- HTTPS: 103 alive / 27 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47559
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
