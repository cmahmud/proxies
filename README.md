# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 332
- HTTP: 103 alive / 38 gold
- HTTPS: 85 alive / 5 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 186 alive / 137 gold

## Historical pool

- Discovered: 171581
- Ever alive: 32897
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
