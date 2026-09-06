# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 390
- HTTP: 106 alive / 72 gold
- HTTPS: 35 alive / 16 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 182 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48232
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
