# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 423
- HTTP: 89 alive / 66 gold
- HTTPS: 88 alive / 28 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47131
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
