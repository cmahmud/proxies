# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 437
- HTTP: 111 alive / 76 gold
- HTTPS: 83 alive / 28 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 205 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45462
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
