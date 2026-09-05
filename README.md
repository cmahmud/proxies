# SyndProxy validated proxy pool

## Current pool

- Alive now: 387
- Gold now: 305
- HTTP: 103 alive / 75 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 75 alive / 70 gold
- SOCKS5: 173 alive / 144 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47836
- Ever gold: 1498

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
