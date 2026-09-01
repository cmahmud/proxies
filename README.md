# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 459
- HTTP: 138 alive / 89 gold
- HTTPS: 142 alive / 34 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46690
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
