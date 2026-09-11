# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 438
- HTTP: 110 alive / 79 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 194 alive / 169 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49103
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
