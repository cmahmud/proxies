# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 390
- HTTP: 88 alive / 62 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 167 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43649
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
