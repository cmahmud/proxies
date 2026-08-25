# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 427
- HTTP: 152 alive / 71 gold
- HTTPS: 72 alive / 20 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 206 alive / 175 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36020
- Ever gold: 1263

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
