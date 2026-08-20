# SyndProxy private pool

## Current pool

- Alive now: 1224
- Gold now: 566
- HTTP: 491 alive / 193 gold
- HTTPS: 316 alive / 98 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 197 alive / 132 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22785
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
