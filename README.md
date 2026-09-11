# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 426
- HTTP: 97 alive / 72 gold
- HTTPS: 56 alive / 25 gold
- SOCKS4: 199 alive / 167 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49080
- Ever gold: 1572

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
