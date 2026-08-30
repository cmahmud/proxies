# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 438
- HTTP: 134 alive / 84 gold
- HTTPS: 66 alive / 28 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44301
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
