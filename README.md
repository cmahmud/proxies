# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 469
- HTTP: 136 alive / 95 gold
- HTTPS: 111 alive / 40 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 202 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44849
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
