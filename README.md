# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 424
- HTTP: 116 alive / 80 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 203 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44332
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
