# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 426
- HTTP: 102 alive / 69 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35736
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
