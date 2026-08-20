# SyndProxy private pool

## Current pool

- Alive now: 1235
- Gold now: 563
- HTTP: 446 alive / 181 gold
- HTTPS: 316 alive / 91 gold
- SOCKS4: 230 alive / 132 gold
- SOCKS5: 243 alive / 159 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22955
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
