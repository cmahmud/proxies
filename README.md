# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 426
- HTTP: 93 alive / 72 gold
- HTTPS: 52 alive / 25 gold
- SOCKS4: 196 alive / 169 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49083
- Ever gold: 1572

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
