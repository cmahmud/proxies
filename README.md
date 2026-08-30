# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 444
- HTTP: 131 alive / 87 gold
- HTTPS: 68 alive / 34 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 207 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44236
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
