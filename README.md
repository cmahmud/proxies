# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 380
- HTTP: 93 alive / 66 gold
- HTTPS: 42 alive / 25 gold
- SOCKS4: 162 alive / 118 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48730
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
