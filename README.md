# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 483
- HTTP: 137 alive / 101 gold
- HTTPS: 119 alive / 45 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44935
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
