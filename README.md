# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 453
- HTTP: 148 alive / 89 gold
- HTTPS: 118 alive / 31 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 239 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45320
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
