# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 420
- HTTP: 101 alive / 65 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35747
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
