# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 390
- HTTP: 83 alive / 61 gold
- HTTPS: 51 alive / 21 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 167 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43648
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
