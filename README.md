# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 424
- HTTP: 98 alive / 66 gold
- HTTPS: 70 alive / 27 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47058
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
