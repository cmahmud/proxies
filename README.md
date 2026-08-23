# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 393
- HTTP: 108 alive / 64 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33157
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
