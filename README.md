# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 435
- HTTP: 120 alive / 76 gold
- HTTPS: 94 alive / 27 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 206 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
