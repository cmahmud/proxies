# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 454
- HTTP: 123 alive / 87 gold
- HTTPS: 111 alive / 34 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45608
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
