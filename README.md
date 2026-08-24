# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 403
- HTTP: 124 alive / 77 gold
- HTTPS: 56 alive / 15 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 193 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33274
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
