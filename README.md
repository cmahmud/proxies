# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 361
- HTTP: 107 alive / 36 gold
- HTTPS: 51 alive / 11 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32937
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
