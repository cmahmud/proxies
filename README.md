# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 300
- HTTP: 112 alive / 74 gold
- HTTPS: 45 alive / 23 gold
- SOCKS4: 79 alive / 66 gold
- SOCKS5: 154 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47874
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
