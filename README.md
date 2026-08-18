# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 240
- HTTP: 290 alive / 35 gold
- HTTPS: 171 alive / 8 gold
- SOCKS4: 261 alive / 131 gold
- SOCKS5: 205 alive / 66 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
