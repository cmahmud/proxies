# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 314
- HTTP: 93 alive / 59 gold
- HTTPS: 37 alive / 20 gold
- SOCKS4: 115 alive / 104 gold
- SOCKS5: 145 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49516
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
