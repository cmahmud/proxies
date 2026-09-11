# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 352
- HTTP: 108 alive / 72 gold
- HTTPS: 45 alive / 19 gold
- SOCKS4: 95 alive / 90 gold
- SOCKS5: 175 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48693
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
