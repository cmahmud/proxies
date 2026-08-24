# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 402
- HTTP: 146 alive / 69 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 197 alive / 164 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
