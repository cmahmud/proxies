# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 422
- HTTP: 92 alive / 64 gold
- HTTPS: 78 alive / 28 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45489
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
