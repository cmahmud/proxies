# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 418
- HTTP: 95 alive / 74 gold
- HTTPS: 42 alive / 24 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 171 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49455
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
