# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 451
- HTTP: 132 alive / 85 gold
- HTTPS: 142 alive / 32 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46850
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
