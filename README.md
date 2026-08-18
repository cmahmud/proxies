# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 240
- HTTP: 239 alive / 29 gold
- HTTPS: 116 alive / 8 gold
- SOCKS4: 233 alive / 136 gold
- SOCKS5: 190 alive / 67 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
