# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 371
- HTTP: 78 alive / 45 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 172318
- Ever alive: 32976
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
