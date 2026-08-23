# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 389
- HTTP: 116 alive / 66 gold
- HTTPS: 57 alive / 13 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 195 alive / 157 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33172
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
