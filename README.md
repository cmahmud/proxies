# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 453
- HTTP: 99 alive / 77 gold
- HTTPS: 108 alive / 33 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47428
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
