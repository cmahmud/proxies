# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 472
- HTTP: 134 alive / 100 gold
- HTTPS: 61 alive / 37 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49364
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
