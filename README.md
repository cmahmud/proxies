# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 461
- HTTP: 122 alive / 89 gold
- HTTPS: 129 alive / 35 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46709
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
