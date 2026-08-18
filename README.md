# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 240
- HTTP: 261 alive / 33 gold
- HTTPS: 141 alive / 8 gold
- SOCKS4: 256 alive / 134 gold
- SOCKS5: 198 alive / 65 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
