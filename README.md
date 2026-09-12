# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 425
- HTTP: 104 alive / 78 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49452
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
