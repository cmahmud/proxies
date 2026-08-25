# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 417
- HTTP: 107 alive / 63 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36071
- Ever gold: 1266

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
