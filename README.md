# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 368
- HTTP: 78 alive / 46 gold
- HTTPS: 30 alive / 15 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 179 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48314
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
