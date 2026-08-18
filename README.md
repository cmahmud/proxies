# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 240
- HTTP: 235 alive / 29 gold
- HTTPS: 146 alive / 8 gold
- SOCKS4: 236 alive / 136 gold
- SOCKS5: 189 alive / 67 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
