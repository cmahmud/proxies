# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 199
- HTTP: 174 alive / 43 gold
- HTTPS: 63 alive / 6 gold
- SOCKS4: 93 alive / 68 gold
- SOCKS5: 130 alive / 82 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32753
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
