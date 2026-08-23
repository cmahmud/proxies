# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 392
- HTTP: 115 alive / 66 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 171 alive / 153 gold
- SOCKS5: 189 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33169
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
