# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 438
- HTTP: 119 alive / 91 gold
- HTTPS: 68 alive / 35 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44093
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
