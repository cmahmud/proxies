# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 451
- HTTP: 124 alive / 93 gold
- HTTPS: 66 alive / 36 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 199 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44255
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
