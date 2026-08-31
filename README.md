# SyndProxy validated proxy pool

## Current pool

- Alive now: 709
- Gold now: 453
- HTTP: 162 alive / 89 gold
- HTTPS: 126 alive / 30 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 244 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45318
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
