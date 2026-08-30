# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 444
- HTTP: 123 alive / 80 gold
- HTTPS: 113 alive / 35 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44644
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
