# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 424
- HTTP: 112 alive / 69 gold
- HTTPS: 66 alive / 28 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47056
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
