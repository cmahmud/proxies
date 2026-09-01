# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 425
- HTTP: 120 alive / 70 gold
- HTTPS: 74 alive / 28 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47053
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
