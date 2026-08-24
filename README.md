# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 396
- HTTP: 113 alive / 63 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33654
- Ever gold: 1246

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
