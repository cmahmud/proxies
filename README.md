# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 426
- HTTP: 98 alive / 69 gold
- HTTPS: 64 alive / 29 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47069
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
