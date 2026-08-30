# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 443
- HTTP: 126 alive / 82 gold
- HTTPS: 71 alive / 29 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44596
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
