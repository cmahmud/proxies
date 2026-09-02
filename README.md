# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 439
- HTTP: 97 alive / 70 gold
- HTTPS: 104 alive / 31 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 183 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47447
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
