# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 444
- HTTP: 117 alive / 77 gold
- HTTPS: 138 alive / 37 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44666
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
