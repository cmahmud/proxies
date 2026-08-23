# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 392
- HTTP: 120 alive / 66 gold
- HTTPS: 63 alive / 13 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33168
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
