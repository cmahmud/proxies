# SyndProxy validated proxy pool

## Current pool

- Alive now: 338
- Gold now: 206
- HTTP: 106 alive / 48 gold
- HTTPS: 41 alive / 6 gold
- SOCKS4: 82 alive / 64 gold
- SOCKS5: 109 alive / 88 gold

## Historical pool

- Discovered: 170283
- Ever alive: 32758
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
