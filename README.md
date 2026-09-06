# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 392
- HTTP: 104 alive / 74 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 165 alive / 149 gold
- SOCKS5: 170 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48206
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
