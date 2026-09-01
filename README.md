# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 463
- HTTP: 132 alive / 92 gold
- HTTPS: 120 alive / 36 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 222 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46496
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
