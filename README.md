# SyndProxy private pool

## Current pool

- Alive now: 1577
- Gold now: 613
- HTTP: 613 alive / 214 gold
- HTTPS: 511 alive / 120 gold
- SOCKS4: 220 alive / 135 gold
- SOCKS5: 233 alive / 144 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23766
- Ever gold: 957

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
