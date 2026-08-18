# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 240
- HTTP: 263 alive / 33 gold
- HTTPS: 134 alive / 8 gold
- SOCKS4: 254 alive / 134 gold
- SOCKS5: 194 alive / 65 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
