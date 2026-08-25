# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 420
- HTTP: 104 alive / 63 gold
- HTTPS: 87 alive / 24 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35800
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
