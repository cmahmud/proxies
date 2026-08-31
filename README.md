# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 422
- HTTP: 89 alive / 62 gold
- HTTPS: 72 alive / 28 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45489
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
