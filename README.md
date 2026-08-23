# SyndProxy validated proxy pool

## Current pool

- Alive now: 342
- Gold now: 204
- HTTP: 106 alive / 47 gold
- HTTPS: 45 alive / 6 gold
- SOCKS4: 82 alive / 64 gold
- SOCKS5: 109 alive / 87 gold

## Historical pool

- Discovered: 170283
- Ever alive: 32758
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
