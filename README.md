# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 452
- HTTP: 129 alive / 95 gold
- HTTPS: 57 alive / 30 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49326
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
