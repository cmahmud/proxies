# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 408
- HTTP: 97 alive / 72 gold
- HTTPS: 32 alive / 15 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48247
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
