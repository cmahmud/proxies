# SyndProxy validated proxy pool

## Current pool

- Alive now: 397
- Gold now: 308
- HTTP: 106 alive / 75 gold
- HTTPS: 35 alive / 20 gold
- SOCKS4: 85 alive / 70 gold
- SOCKS5: 171 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47830
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
