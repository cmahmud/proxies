# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 465
- HTTP: 136 alive / 94 gold
- HTTPS: 116 alive / 37 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 204 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44853
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
