# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 446
- HTTP: 149 alive / 81 gold
- HTTPS: 95 alive / 32 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 226 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45440
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
