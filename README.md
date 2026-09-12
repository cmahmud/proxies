# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 423
- HTTP: 105 alive / 74 gold
- HTTPS: 47 alive / 25 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49480
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
