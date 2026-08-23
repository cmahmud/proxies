# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 347
- HTTP: 115 alive / 40 gold
- HTTPS: 75 alive / 11 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 182 alive / 144 gold

## Historical pool

- Discovered: 171038
- Ever alive: 32815
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
