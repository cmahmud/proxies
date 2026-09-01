# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 441
- HTTP: 113 alive / 80 gold
- HTTPS: 82 alive / 29 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 186 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47012
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
