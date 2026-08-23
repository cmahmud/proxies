# SyndProxy validated proxy pool

## Current pool

- Alive now: 368
- Gold now: 205
- HTTP: 112 alive / 47 gold
- HTTPS: 63 alive / 8 gold
- SOCKS4: 74 alive / 65 gold
- SOCKS5: 119 alive / 85 gold

## Historical pool

- Discovered: 169854
- Ever alive: 32700
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
