# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 377
- HTTP: 86 alive / 64 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 145 alive / 121 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48737
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
