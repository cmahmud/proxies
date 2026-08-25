# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 424
- HTTP: 119 alive / 76 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34883
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
