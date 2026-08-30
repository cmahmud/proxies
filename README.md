# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 463
- HTTP: 126 alive / 95 gold
- HTTPS: 114 alive / 37 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44822
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
