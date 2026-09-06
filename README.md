# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 394
- HTTP: 106 alive / 71 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48221
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
