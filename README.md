# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 428
- HTTP: 129 alive / 70 gold
- HTTPS: 65 alive / 22 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36023
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
