# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 393
- HTTP: 109 alive / 61 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33654
- Ever gold: 1246

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
