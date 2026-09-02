# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 449
- HTTP: 105 alive / 75 gold
- HTTPS: 117 alive / 31 gold
- SOCKS4: 182 alive / 165 gold
- SOCKS5: 185 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47434
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
