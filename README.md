# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 283
- HTTP: 292 alive / 31 gold
- HTTPS: 209 alive / 6 gold
- SOCKS4: 209 alive / 125 gold
- SOCKS5: 216 alive / 121 gold

## Historical pool

- Discovered: 102843
- Ever alive: 13200
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
