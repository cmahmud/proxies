# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 435
- HTTP: 127 alive / 90 gold
- HTTPS: 73 alive / 34 gold
- SOCKS4: 157 alive / 151 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44077
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
