# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 438
- HTTP: 115 alive / 77 gold
- HTTPS: 79 alive / 28 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 205 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45462
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
