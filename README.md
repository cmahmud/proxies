# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 381
- HTTP: 138 alive / 77 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 161 alive / 132 gold
- SOCKS5: 179 alive / 148 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48020
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
