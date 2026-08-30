# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 444
- HTTP: 122 alive / 80 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44644
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
