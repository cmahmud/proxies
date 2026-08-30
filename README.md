# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 436
- HTTP: 126 alive / 90 gold
- HTTPS: 75 alive / 34 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 171 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44077
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
