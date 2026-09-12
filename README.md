# SyndProxy validated proxy pool

## Current pool

- Alive now: 409
- Gold now: 346
- HTTP: 85 alive / 66 gold
- HTTPS: 34 alive / 17 gold
- SOCKS4: 134 alive / 121 gold
- SOCKS5: 156 alive / 142 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49550
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
