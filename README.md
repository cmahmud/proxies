# SyndProxy private pool

## Current pool

- Alive now: 667
- Gold now: 387
- HTTP: 169 alive / 69 gold
- HTTPS: 91 alive / 21 gold
- SOCKS4: 196 alive / 142 gold
- SOCKS5: 211 alive / 155 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25563
- Ever gold: 1065

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
