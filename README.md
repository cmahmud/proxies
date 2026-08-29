# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 385
- HTTP: 89 alive / 65 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 164 alive / 156 gold
- SOCKS5: 165 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43369
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
