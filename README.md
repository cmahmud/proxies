# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 391
- HTTP: 106 alive / 71 gold
- HTTPS: 33 alive / 16 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 180 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48230
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
