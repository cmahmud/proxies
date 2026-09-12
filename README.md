# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 459
- HTTP: 131 alive / 97 gold
- HTTPS: 62 alive / 33 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49329
- Ever gold: 1577

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
