# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 379
- HTTP: 79 alive / 52 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 175243
- Ever alive: 33123
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
