# SyndProxy validated proxy pool

## Current pool

- Alive now: 711
- Gold now: 452
- HTTP: 162 alive / 87 gold
- HTTPS: 133 alive / 30 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 241 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45317
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
