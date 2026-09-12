# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 453
- HTTP: 122 alive / 94 gold
- HTTPS: 59 alive / 32 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49327
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
