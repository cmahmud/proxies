# SyndProxy validated proxy pool

## Current pool

- Alive now: 437
- Gold now: 362
- HTTP: 81 alive / 60 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 156 alive / 137 gold
- SOCKS5: 164 alive / 150 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49559
- Ever gold: 1587

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
