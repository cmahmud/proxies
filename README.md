# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 395
- HTTP: 97 alive / 68 gold
- HTTPS: 38 alive / 20 gold
- SOCKS4: 159 alive / 134 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48764
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
