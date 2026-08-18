# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 290
- HTTP: 305 alive / 26 gold
- HTTPS: 171 alive / 4 gold
- SOCKS4: 206 alive / 140 gold
- SOCKS5: 209 alive / 120 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13476
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
