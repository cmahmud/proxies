# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 422
- HTTP: 94 alive / 63 gold
- HTTPS: 74 alive / 29 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45489
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
