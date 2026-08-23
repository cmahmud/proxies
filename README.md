# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 371
- HTTP: 98 alive / 58 gold
- HTTPS: 33 alive / 8 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 173 alive / 154 gold

## Historical pool

- Discovered: 174309
- Ever alive: 33084
- Ever gold: 1225

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
