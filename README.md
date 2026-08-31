# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 454
- HTTP: 135 alive / 85 gold
- HTTPS: 95 alive / 36 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45586
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
