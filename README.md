# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 434
- HTTP: 113 alive / 76 gold
- HTTPS: 56 alive / 25 gold
- SOCKS4: 191 alive / 169 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49107
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
