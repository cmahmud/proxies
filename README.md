# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 439
- HTTP: 146 alive / 75 gold
- HTTPS: 96 alive / 30 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 206 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45395
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
