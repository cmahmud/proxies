# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 438
- HTTP: 99 alive / 78 gold
- HTTPS: 91 alive / 26 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47679
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
