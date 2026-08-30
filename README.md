# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 435
- HTTP: 111 alive / 74 gold
- HTTPS: 98 alive / 33 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44615
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
