# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 363
- HTTP: 86 alive / 61 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 158 alive / 136 gold
- SOCKS5: 163 alive / 150 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49559
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
