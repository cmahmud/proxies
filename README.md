# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 449
- HTTP: 127 alive / 93 gold
- HTTPS: 71 alive / 33 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 207 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44237
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
