# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 449
- HTTP: 99 alive / 75 gold
- HTTPS: 106 alive / 30 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 191 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47437
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
