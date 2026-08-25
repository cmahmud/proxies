# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 420
- HTTP: 103 alive / 66 gold
- HTTPS: 83 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 198 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36046
- Ever gold: 1265

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
