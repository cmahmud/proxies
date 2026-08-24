# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 396
- HTTP: 148 alive / 64 gold
- HTTPS: 65 alive / 15 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
