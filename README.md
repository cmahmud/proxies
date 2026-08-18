# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 239
- HTTP: 232 alive / 31 gold
- HTTPS: 123 alive / 8 gold
- SOCKS4: 246 alive / 134 gold
- SOCKS5: 191 alive / 66 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9662
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
