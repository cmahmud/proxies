# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 293
- HTTP: 142 alive / 70 gold
- HTTPS: 177 alive / 35 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 138 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48481
- Ever gold: 1541

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
