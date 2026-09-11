# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 429
- HTTP: 99 alive / 73 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 197 alive / 170 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49089
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
