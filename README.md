# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 422
- HTTP: 87 alive / 66 gold
- HTTPS: 59 alive / 24 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47073
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
