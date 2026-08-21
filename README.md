# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 421
- HTTP: 190 alive / 79 gold
- HTTPS: 149 alive / 25 gold
- SOCKS4: 211 alive / 148 gold
- SOCKS5: 250 alive / 169 gold

## Historical pool

- Discovered: 155791
- Ever alive: 29332
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
