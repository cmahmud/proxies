# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 387
- HTTP: 143 alive / 81 gold
- HTTPS: 56 alive / 24 gold
- SOCKS4: 161 alive / 132 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48019
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
