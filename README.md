# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 392
- HTTP: 93 alive / 66 gold
- HTTPS: 30 alive / 16 gold
- SOCKS4: 160 alive / 140 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48777
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
