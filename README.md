# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 445
- HTTP: 111 alive / 81 gold
- HTTPS: 106 alive / 28 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47559
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
