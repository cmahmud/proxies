# SyndProxy private pool

## Current pool

- Alive now: 1300
- Gold now: 550
- HTTP: 474 alive / 177 gold
- HTTPS: 350 alive / 82 gold
- SOCKS4: 235 alive / 132 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22976
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
