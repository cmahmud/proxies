# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 427
- HTTP: 122 alive / 79 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 201 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44337
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
