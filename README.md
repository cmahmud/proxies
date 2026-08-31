# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 484
- HTTP: 142 alive / 99 gold
- HTTPS: 119 alive / 45 gold
- SOCKS4: 176 alive / 164 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45100
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
