# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 371
- HTTP: 81 alive / 45 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 172318
- Ever alive: 32975
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
