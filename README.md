# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 390
- HTTP: 95 alive / 66 gold
- HTTPS: 33 alive / 15 gold
- SOCKS4: 156 alive / 140 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48777
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
