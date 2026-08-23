# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 200
- HTTP: 179 alive / 44 gold
- HTTPS: 56 alive / 6 gold
- SOCKS4: 105 alive / 66 gold
- SOCKS5: 154 alive / 84 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32733
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
