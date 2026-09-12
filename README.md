# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 425
- HTTP: 115 alive / 80 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49473
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
