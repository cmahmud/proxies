# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 393
- HTTP: 118 alive / 66 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33168
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
