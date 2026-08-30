# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 443
- HTTP: 114 alive / 79 gold
- HTTPS: 120 alive / 35 gold
- SOCKS4: 161 alive / 159 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44639
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
