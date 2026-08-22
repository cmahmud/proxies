# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 340
- HTTP: 240 alive / 79 gold
- HTTPS: 159 alive / 23 gold
- SOCKS4: 177 alive / 113 gold
- SOCKS5: 213 alive / 125 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32579
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
