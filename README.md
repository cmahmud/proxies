# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 453
- HTTP: 120 alive / 86 gold
- HTTPS: 71 alive / 34 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45568
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
