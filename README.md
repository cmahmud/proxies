# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 450
- HTTP: 130 alive / 84 gold
- HTTPS: 130 alive / 32 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46845
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
