# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 419
- HTTP: 111 alive / 75 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44489
- Ever gold: 1402

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
