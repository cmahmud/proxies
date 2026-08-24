# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 409
- HTTP: 108 alive / 67 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33659
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
