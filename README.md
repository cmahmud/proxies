# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 483
- HTTP: 138 alive / 101 gold
- HTTPS: 120 alive / 45 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44935
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
