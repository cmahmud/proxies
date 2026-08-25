# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 421
- HTTP: 83 alive / 63 gold
- HTTPS: 75 alive / 21 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36116
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
