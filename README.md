# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 437
- HTTP: 108 alive / 75 gold
- HTTPS: 61 alive / 29 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45553
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
