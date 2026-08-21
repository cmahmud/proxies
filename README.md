# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 349
- HTTP: 237 alive / 76 gold
- HTTPS: 149 alive / 21 gold
- SOCKS4: 203 alive / 120 gold
- SOCKS5: 210 alive / 132 gold

## Historical pool

- Discovered: 157663
- Ever alive: 29782
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
