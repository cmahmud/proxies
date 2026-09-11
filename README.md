# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 431
- HTTP: 104 alive / 69 gold
- HTTPS: 49 alive / 20 gold
- SOCKS4: 196 alive / 167 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48905
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
