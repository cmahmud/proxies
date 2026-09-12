# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 433
- HTTP: 108 alive / 81 gold
- HTTPS: 45 alive / 30 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 175 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49447
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
