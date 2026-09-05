# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 298
- HTTP: 104 alive / 79 gold
- HTTPS: 51 alive / 21 gold
- SOCKS4: 74 alive / 65 gold
- SOCKS5: 153 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47919
- Ever gold: 1504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
