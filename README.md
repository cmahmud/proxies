# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 423
- HTTP: 105 alive / 67 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35742
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
