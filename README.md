# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 416
- HTTP: 113 alive / 64 gold
- HTTPS: 73 alive / 22 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 202 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
