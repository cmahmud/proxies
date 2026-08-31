# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 441
- HTTP: 123 alive / 80 gold
- HTTPS: 97 alive / 26 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 198 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
