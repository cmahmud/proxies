# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 409
- HTTP: 106 alive / 67 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33658
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
