# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 453
- HTTP: 133 alive / 86 gold
- HTTPS: 89 alive / 36 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45603
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
