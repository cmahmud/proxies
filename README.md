# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 206
- HTTP: 116 alive / 45 gold
- HTTPS: 73 alive / 6 gold
- SOCKS4: 85 alive / 67 gold
- SOCKS5: 112 alive / 88 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32755
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
