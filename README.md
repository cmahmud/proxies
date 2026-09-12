# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 455
- HTTP: 123 alive / 94 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49317
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
