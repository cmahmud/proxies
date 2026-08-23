# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 359
- HTTP: 101 alive / 36 gold
- HTTPS: 48 alive / 11 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 171600
- Ever alive: 32940
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
