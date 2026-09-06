# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 394
- HTTP: 110 alive / 74 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 168 alive / 150 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48226
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
