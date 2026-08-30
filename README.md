# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 438
- HTTP: 110 alive / 75 gold
- HTTPS: 97 alive / 34 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44615
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
