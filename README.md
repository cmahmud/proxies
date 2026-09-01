# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 463
- HTTP: 128 alive / 92 gold
- HTTPS: 129 alive / 34 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 225 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46524
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
