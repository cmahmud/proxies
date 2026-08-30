# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 450
- HTTP: 143 alive / 89 gold
- HTTPS: 79 alive / 35 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 214 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44220
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
