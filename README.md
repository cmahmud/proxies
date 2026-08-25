# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 413
- HTTP: 93 alive / 64 gold
- HTTPS: 87 alive / 20 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35517
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
