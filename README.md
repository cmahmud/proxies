# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 418
- HTTP: 102 alive / 61 gold
- HTTPS: 91 alive / 23 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35757
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
