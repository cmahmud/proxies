# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 451
- HTTP: 118 alive / 82 gold
- HTTPS: 85 alive / 35 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47002
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
