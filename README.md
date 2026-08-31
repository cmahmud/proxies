# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 438
- HTTP: 117 alive / 77 gold
- HTTPS: 64 alive / 27 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45548
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
