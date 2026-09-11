# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 444
- HTTP: 121 alive / 86 gold
- HTTPS: 55 alive / 27 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49265
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
