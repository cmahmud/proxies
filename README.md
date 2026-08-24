# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 393
- HTTP: 114 alive / 68 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 176968
- Ever alive: 33260
- Ever gold: 1232

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
