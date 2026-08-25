# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 417
- HTTP: 89 alive / 62 gold
- HTTPS: 77 alive / 19 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36128
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
