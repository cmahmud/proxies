# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 446
- HTTP: 117 alive / 88 gold
- HTTPS: 56 alive / 31 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49304
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
