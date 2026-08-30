# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 427
- HTTP: 111 alive / 74 gold
- HTTPS: 58 alive / 26 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 201 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44469
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
