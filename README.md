# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 449
- HTTP: 106 alive / 76 gold
- HTTPS: 108 alive / 32 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47422
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
