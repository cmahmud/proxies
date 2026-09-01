# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 450
- HTTP: 95 alive / 74 gold
- HTTPS: 113 alive / 35 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47402
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
