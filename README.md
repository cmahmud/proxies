# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 412
- HTTP: 85 alive / 65 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 175 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47236
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
