# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 403
- HTTP: 120 alive / 76 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 192 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33274
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
