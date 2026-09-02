# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 444
- HTTP: 109 alive / 81 gold
- HTTPS: 101 alive / 28 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47559
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
