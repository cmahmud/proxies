# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 464
- HTTP: 129 alive / 100 gold
- HTTPS: 61 alive / 32 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49334
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
