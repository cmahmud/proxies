# SyndProxy validated proxy pool

## Current pool

- Alive now: 439
- Gold now: 332
- HTTP: 92 alive / 57 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 149 alive / 132 gold
- SOCKS5: 145 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48345
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
