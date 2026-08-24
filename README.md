# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 402
- HTTP: 118 alive / 75 gold
- HTTPS: 55 alive / 15 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 193 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33275
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
