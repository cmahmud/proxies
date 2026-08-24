# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 409
- HTTP: 107 alive / 67 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33659
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
