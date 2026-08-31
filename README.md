# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 443
- HTTP: 128 alive / 79 gold
- HTTPS: 68 alive / 30 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45559
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
