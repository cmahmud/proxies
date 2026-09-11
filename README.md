# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 432
- HTTP: 106 alive / 74 gold
- HTTPS: 56 alive / 26 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49131
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
