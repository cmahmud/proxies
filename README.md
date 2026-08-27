# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 418
- HTTP: 101 alive / 71 gold
- HTTPS: 107 alive / 24 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41816
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
