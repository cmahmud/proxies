# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 442
- HTTP: 142 alive / 76 gold
- HTTPS: 103 alive / 32 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 208 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45393
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
