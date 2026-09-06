# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 335
- HTTP: 80 alive / 59 gold
- HTTPS: 40 alive / 16 gold
- SOCKS4: 153 alive / 137 gold
- SOCKS5: 149 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48354
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
