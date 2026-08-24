# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 383
- HTTP: 90 alive / 45 gold
- HTTPS: 51 alive / 13 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33567
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
