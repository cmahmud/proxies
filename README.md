# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 359
- HTTP: 96 alive / 68 gold
- HTTPS: 54 alive / 22 gold
- SOCKS4: 125 alive / 100 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48713
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
