# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 440
- HTTP: 118 alive / 81 gold
- HTTPS: 72 alive / 32 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44298
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
