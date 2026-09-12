# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 450
- HTTP: 126 alive / 91 gold
- HTTPS: 53 alive / 30 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49316
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
