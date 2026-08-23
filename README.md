# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 392
- HTTP: 120 alive / 65 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33167
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
