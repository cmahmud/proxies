# SyndProxy validated proxy pool

## Current pool

- Alive now: 385
- Gold now: 300
- HTTP: 105 alive / 79 gold
- HTTPS: 55 alive / 21 gold
- SOCKS4: 72 alive / 65 gold
- SOCKS5: 153 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47919
- Ever gold: 1504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
