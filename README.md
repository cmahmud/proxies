# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 346
- HTTP: 115 alive / 39 gold
- HTTPS: 81 alive / 11 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 180 alive / 144 gold

## Historical pool

- Discovered: 171038
- Ever alive: 32815
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
