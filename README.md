# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 354
- HTTP: 134 alive / 79 gold
- HTTPS: 84 alive / 31 gold
- SOCKS4: 191 alive / 65 gold
- SOCKS5: 253 alive / 179 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48576
- Ever gold: 1546

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
