# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 426
- HTTP: 115 alive / 73 gold
- HTTPS: 75 alive / 28 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47051
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
