# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 359
- HTTP: 105 alive / 70 gold
- HTTPS: 54 alive / 21 gold
- SOCKS4: 122 alive / 99 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48713
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
