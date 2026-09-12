# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 424
- HTTP: 118 alive / 79 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 185 alive / 160 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49473
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
