# SyndProxy validated proxy pool

## Current pool

- Alive now: 401
- Gold now: 336
- HTTP: 82 alive / 65 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 130 alive / 116 gold
- SOCKS5: 152 alive / 138 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49549
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
