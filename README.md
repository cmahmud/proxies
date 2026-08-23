# SyndProxy validated proxy pool

## Current pool

- Alive now: 456
- Gold now: 378
- HTTP: 76 alive / 47 gold
- HTTPS: 36 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 173029
- Ever alive: 32987
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
