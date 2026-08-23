# SyndProxy validated proxy pool

## Current pool

- Alive now: 368
- Gold now: 206
- HTTP: 107 alive / 45 gold
- HTTPS: 62 alive / 8 gold
- SOCKS4: 73 alive / 67 gold
- SOCKS5: 126 alive / 86 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32710
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
