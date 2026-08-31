# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 410
- HTTP: 91 alive / 58 gold
- HTTPS: 66 alive / 21 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45504
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
