# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 393
- HTTP: 98 alive / 51 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41661
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
