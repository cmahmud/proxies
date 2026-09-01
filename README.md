# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 426
- HTTP: 105 alive / 67 gold
- HTTPS: 73 alive / 31 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 173 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47056
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
