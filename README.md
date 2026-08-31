# SyndProxy validated proxy pool

## Current pool

- Alive now: 703
- Gold now: 453
- HTTP: 161 alive / 89 gold
- HTTPS: 126 alive / 29 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 241 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45317
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
