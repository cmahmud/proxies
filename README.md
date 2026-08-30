# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 437
- HTTP: 133 alive / 91 gold
- HTTPS: 71 alive / 33 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44078
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
