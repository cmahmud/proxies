# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 437
- HTTP: 110 alive / 76 gold
- HTTPS: 62 alive / 28 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45550
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
