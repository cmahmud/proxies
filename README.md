# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 416
- HTTP: 86 alive / 64 gold
- HTTPS: 49 alive / 18 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48885
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
