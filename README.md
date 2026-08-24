# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 386
- HTTP: 101 alive / 57 gold
- HTTPS: 43 alive / 8 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 187 alive / 163 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33319
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
