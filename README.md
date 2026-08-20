# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 394
- HTTP: 169 alive / 71 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 216 alive / 155 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26021
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
