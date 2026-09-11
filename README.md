# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 423
- HTTP: 89 alive / 67 gold
- HTTPS: 49 alive / 22 gold
- SOCKS4: 187 alive / 165 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48896
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
